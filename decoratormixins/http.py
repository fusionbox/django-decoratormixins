from django.views.decorators.http import (
    conditional_page, require_GET, require_POST, require_safe, etag, last_modified
)

from . import DecoratorMixin

ConditionalPageMixin = DecoratorMixin(conditional_page)
RequireGetMixin = DecoratorMixin(require_GET)
RequirePostMixin = DecoratorMixin(require_POST)
RequireSafeMixin = DecoratorMixin(require_safe)
EtagMixin = DecoratorMixin(etag)
LastModifiedMixin = DecoratorMixin(last_modified)
