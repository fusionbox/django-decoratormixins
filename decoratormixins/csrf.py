from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt

from . import DecoratorMixin

CsrfProtectMixin = DecoratorMixin(csrf_protect)
EnsureCsrfCookieMixin = DecoratorMixin(ensure_csrf_cookie)
CsrfExemptMixin = DecoratorMixin(csrf_exempt)
