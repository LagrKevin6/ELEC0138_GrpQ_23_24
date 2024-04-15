# defining a middleware for counting visits, as ddos may fail to be counted in view.py
from .models import PageVisit
from django.utils.timezone import now

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request path and timestamp before processing the request
        PageVisit.objects.create(path=request.path, timestamp=now())
        
        # Get the response from the next middleware or view
        response = self.get_response(request)

        return response
