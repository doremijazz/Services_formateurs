from django.urls import path

from . import views

app_name = "Services"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('do_request', views.do_request, name='do_request'),
    ]