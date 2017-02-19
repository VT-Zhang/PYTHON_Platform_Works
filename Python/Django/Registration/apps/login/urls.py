from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    # url(r'^goback$', views.goback),
    # url(r'^delete/(?P<id>\d+)$', views.delete),
]
