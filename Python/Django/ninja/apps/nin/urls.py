from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.all),
    url(r'^ninjas/(?P<color>\w+)$',  views.color),
]
