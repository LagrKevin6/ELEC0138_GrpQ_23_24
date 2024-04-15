from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt  # Disabling CSRF

import logging
logger = logging.getLogger(__name__)
from .models import LoginAttempt

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
        LoginAttempt.objects.create(username=username, password=password)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("You are logged in.",header = {"status":True})
        else:
            return HttpResponse("Login failed.",header = {"status":False})
    return render(request, 'user_login.html')


def view_logins(request):
    attempts = LoginAttempt.objects.all()
    return render(request, 'view_details.html', {'attempts': attempts})