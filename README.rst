======================
Django-DecoratorMixins
======================

A collection of class-based view mixins for
Django. Django-Decoratormixins also includes a function for converting
view decorators into class-based view mixins.

-----
Usage
-----

If you have a decorator, usage is as simple as calling
``DecoratorMixin`` and passing the decorator as the argument.

.. code:: python

  from decoratormixins import DecoratorMixin

  def my_decorator(f):
      # ...

  MyDecMixin = DecoratorMixin(my_decorator)

~~~~~~~~~~~~~~~~~~~
Decorator Factories
~~~~~~~~~~~~~~~~~~~

Many of Django's built in decorators are actually decorator
factories. In this case, it is necessary to get a decorator out of
them before it is possible to create a mixin from it.

Here we have a decorator factory that modifies a view to require a
certain parameter in a get request:

.. code:: python

  def require_get_param(param):
      def actual_decorator(view_func):
          @wraps(view_func)
          def _wrapped_view_func(request, *args, **kwargs):
              if request.GET.get(param, None) is not None:
                  response = view_func(request, *args, **kwargs)
                  response.content += param
                  return response
              else:
                  return HttpResponseNotFound("{} is not present.".format(param))

          return _wrapped_view_func
      return actual_decorator

In order to use it, we must specify the parameter we are requiring:

.. code:: python

  require_foo_decorator = require_get_param('foo')

And now we can call DecoratorMixin on that decorator:

.. code:: python

  RequireFooMixin = DecoratorMixin(require_foo_decorator)

~~~~~~~~~~~~~~~
Applying Mixins
~~~~~~~~~~~~~~~

Once you have the mixin you reqire, mix it in with a class-based view.

.. code:: python

  class TestView(View):
      def get(self, request):
          return HttpResponse("OK")

  class TestViewFoo(RequireFooMixin, TestView):
      pass

``TestViewFoo.as_view()`` will return a view method that is usable in
your ``urls.py``.

~~~~~~~~~~~~~~~~
Composing Mixins
~~~~~~~~~~~~~~~~

It is possible to use multiple mixins for a single class, but **order
matters**. The leftmost mixin in a class definition will be the
outermost decorator.

.. code:: python

  from decoratormixins.auth import LoginRequiredMixin
  from decoratormixins.http import RequireGetMixin

  # TestView from above

  class LoggedInGetRequestView(LoginRequiredMixin,
                               RequireGetMixin,
			       TestView):
      pass

---------------
Included Mixins
---------------

Here is a list of all of the included mixins, and the modules in which they can be found.

* ``decoratormixins.auth``

  - ``LoginRequiredMixin``

* ``decoratormixins.csrf``

  - ``CsrfProtectMixin``
  - ``EnsureCsrfCookieMixin``
  - ``CsrfExemptMixin``

* ``decoratormixins.http``

  - ``ConditionalPageMixin``
  - ``RequireGetMixin``
  - ``RequirePostMixin``
  - ``RequireSafeMixin``
  - ``EtagMixin``
  - ``LastModifiedMixin``

* ``decoratormixins.cache``

  - ``NeverCacheMixin``

* ``decoratormixins.clickjacking``

  - ``XFrameOptionsDenyMixin``
  - ``XFrameOptionsDenySameoriginMixin``
  - ``XFrameOptionsDenyExemptMixin``
