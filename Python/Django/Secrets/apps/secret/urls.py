from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^create$', views.create, name='create'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like'),
    url(r'^goto$', views.goto, name='goto'),
    url(r'^goback$', views.goback, name='goback'),
]
