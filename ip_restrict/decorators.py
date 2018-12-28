from django.http import HttpResponse
from django.template.loader import get_template

from ip_restrict import settings


def ip_restriction(func):
    def check_ip(request, *args, **kwargs):

        ip = request.META['REMOTE_ADDR']
        if ip not in settings.ALLOWED_IP_BLOCKS:
            temp = get_template('not_allowed_ip.html')
            result = temp.render({'ip': ip})
            return HttpResponse(result)
        return func(request, *args, **kwargs)

    return check_ip
