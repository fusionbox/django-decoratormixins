__version__ = __import__('pkg_resources').get_distribution('django-decoratormixins').version

def DecoratorMixin(decorator):
    """
    Converts a decorator written for a function view into a mixin for a
    class-based view.

    ::

        LoginRequiredMixin = DecoratorMixin(login_required)

        class MyView(LoginRequiredMixin):
            pass

        class SomeView(DecoratorMixin(some_decorator),
                       DecoratorMixin(something_else)):
            pass

    """

    class Mixin(object):
        __doc__ = decorator.__doc__

        @classmethod
        def as_view(cls, *args, **kwargs):
            view = super(Mixin, cls).as_view(*args, **kwargs)
            return decorator(view)

    Mixin.__name__ = str('DecoratorMixin(%s)' % decorator.__name__)
    return Mixin
