from django.http import HttpResponse
from django.template.loader import get_template

from ip_restrict import settings


class IpRestrictMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META['REMOTE_ADDR']

        if ip not in settings.ALLOWED_IP_BLOCKS:
            temp = get_template('not_allowed_ip.html')
            result = temp.render({'ip': ip})
            return HttpResponse(result)

        response = self.get_response(request)

        return response
