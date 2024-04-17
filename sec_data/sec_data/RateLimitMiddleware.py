from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponseForbidden


timeout_sec = 600
MAX_REQUESTS_PER_IP = 100


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = self.get_client_ip(request)
        # If the access to the website of this ip exceed the MAX_REQUESTS_PER_IP, it will be locked
        if self.is_ip_rate_limited(ip_address):
            return HttpResponseForbidden("Rate limit exceeded.")
        return self.get_response(request)

    def get_client_ip(self, request):
        # Get ip address of client
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def is_ip_rate_limited(self, ip_address):
        # Check if the IP address exceeds the limit
        request_count = cache.get(f'rate_limit:{ip_address}')
        if request_count is None:
            cache.set(f'rate_limit:{ip_address}', 1, timeout=600)
            return False
        elif request_count >= 100:
            return True
        else:
            cache.incr(f'rate_limit:{ip_address}')
            return False