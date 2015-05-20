from django.contrib.auth.decorators import login_required

from . import DecoratorMixin

LoginRequiredMixin = DecoratorMixin(login_required)
