from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.success),
    # url(r'^goback$', views.goback),
    # url(r'^delete/(?P<id>\d+)$', views.delete),
]
