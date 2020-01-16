from .app import app
from django_morepath import make_morepath_view
from django.urls import path, re_path
from django.http import HttpResponse


def some_view(request):
    print("wat")
    return HttpResponse("whatever")


urlpatterns = [
    path("what/", some_view),
    re_path("(.*)", make_morepath_view(app))]
