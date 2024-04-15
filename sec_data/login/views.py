from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt  # Disabling CSRF

import logging
logger = logging.getLogger(__name__)
from .models import LoginAttempt, PageVisit

import matplotlib
matplotlib.use('Agg')  # Use the non-GUI Agg backend for rendering to file
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.db.models.functions import TruncHour
from django.db.models import Count


# Create your views here.
def index(request):
    """
    main page for login func
    
    """
    return HttpResponse('This starts')

### def new(request):


###     return render(request, "user_login.html")

@csrf_exempt  # Disable CSRF protection (intentionally vulnerable)
def new(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # taking logging details, insecure
        logger.warning(f"Login attempt with username: {username} and password: {password}")
        

        # Ensuring username and password are not None
        if not username or not password:
            return HttpResponse("Username or password are required", status=400)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            resp = HttpResponse("You are logged in.", status=200)

            # noting logging details, insecure
            LoginAttempt.objects.create(username=username, password=password)
            #resp["status"]=True
            return resp
        else:
            resp = HttpResponse("Login failed.", status=403)
            #resp["status"]=False
            return resp
    return render(request, 'user_login.html')


def view_logins(request):
    attempts = LoginAttempt.objects.all()
    PageVisit.objects.create(path=request.path)
    return render(request, 'view_details.html', {'attempts': attempts})

def show_visits(request):

    visit_data = (PageVisit.objects
                  .annotate(hour=TruncHour('timestamp'))
                  .values('hour')
                  .annotate(count=Count('id'))
                  .order_by('hour'))

    hours = [data['hour'].hour for data in visit_data if data['hour'] is not None]
    counts = [data['count'] for data in visit_data]

    # Bar graph showing counts
    plt.figure(figsize=(10, 5)) 
    plt.bar(hours, counts, color='blue')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Visits')
    plt.title('Hourly Visits')
    plt.xticks(hours)  # Ensure all hours are labeled
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    buffer.close()

    return render(request, 'show_visits.html', {'graph': graph})
