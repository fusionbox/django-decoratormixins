import unittest
from functools import wraps

from django.http import HttpResponseNotFound, HttpResponse
from django.views.generic.base import View
from django.test.utils import setup_test_environment
from django.test.client import RequestFactory

from . import DecoratorMixin

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

RequireFooMixin = DecoratorMixin(require_get_param('foo'))
RequireBarMixin = DecoratorMixin(require_get_param('bar'))

class TestView(View):
    def get(self, request):
        return HttpResponse("OK")

class TestViewFoo(RequireFooMixin, TestView):
    pass

class TestViewBothMixin(RequireFooMixin, RequireBarMixin, TestView):
    pass

class TestDecoratorMixin(unittest.TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()

    def test_sanity(self):
        request = self.request_factory.get('/test/')
        view = TestView.as_view()
        response = view(request)
        self.assertEqual(200, response.status_code)

    def test_foo_required(self):
        request = self.request_factory.get('/test/')
        view = TestViewFoo.as_view()
        response = view(request)
        self.assertEqual(404, response.status_code)

        request = self.request_factory.get('/test/', data={"foo": 1})
        response = view(request)
        self.assertEqual(200, response.status_code)

    def test_foo_then_bar_required(self):
        request = self.request_factory.get('/test/', data={"foo": 1})
        view = TestViewBothMixin.as_view()
        response = view(request)
        self.assertEqual(404, response.status_code)

        request = self.request_factory.get('/test/', data={"bar": 1})
        view = TestViewBothMixin.as_view()
        response = view(request)
        self.assertEqual(404, response.status_code)

        request = self.request_factory.get('/test/', data={"bar": 1, "foo": 1})
        view = TestViewBothMixin.as_view()
        response = view(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual("OKbarfoo", response.content)
