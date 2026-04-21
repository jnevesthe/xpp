import ipinfo
from django.utils.timezone import now
from .models import TrafficLog

ACCESS_TOKEN = 'SEU_TOKEN_DO_IPINFO'  # se tiver, ou None

class TrafficLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        if ACCESS_TOKEN:
            self.handler = ipinfo.getHandler(ACCESS_TOKEN)
        else:
            self.handler = None

    def __call__(self, request):
        # Pega IP
        ip = self.get_client_ip(request)

        country = city = None
        if self.handler:
            try:
                details = self.handler.getDetails(ip)
                country = details.country_name
                city = details.city
            except:
                pass

        # Salva log
        TrafficLog.objects.create(
            ip=ip,
            country=country,
            city=city,
            path=request.path,
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


from django.shortcuts import render

class Handle404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return render(request, "404.html", status=404)
        return response


from django.utils import translation
from django.conf import settings

class TransMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        lang = translation.get_language_from_request(request, check_path=True)
        supported = [code for code, name in settings.LANGUAGES]

        if lang not in supported:
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'

        response = self.get_response(request)
        return response
