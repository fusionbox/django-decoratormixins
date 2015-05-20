from django.views.decorators.cache import cache_page, cache_control, never_cache

from . import DecoratorMixin

NeverCacheMixin = DecoratorMixin(never_cache)
