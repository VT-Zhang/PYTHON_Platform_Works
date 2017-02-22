from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addnew$', views.addnew, name='addnew'),
    url(r'^create$', views.create, name='create'),
    url(r'^goback$', views.goback, name='goback'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
]
