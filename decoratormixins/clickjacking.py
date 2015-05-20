from django.views.decorators.clickjacking import (
    xframe_options_deny,
    xframe_options_sameorigin,
    xframe_options_exempt
    )

from . import DecoratorMixin

XFrameOptionsDenyMixin = DecoratorMixin(xframe_options_deny)
XFrameOptionsSameoriginMixin = DecoratorMixin(xframe_options_sameorigin)
XFrameOptionsExemptMixin = DecoratorMixin(xframe_options_exempt)
