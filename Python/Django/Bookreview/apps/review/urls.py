from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^goto$', views.goto, name='goto'),
    url(r'^create$', views.create, name='create'),
    url(r'^main$', views.main, name='main'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^book/(?P<id>\d+)$', views.book, name='book'),
    url(r'^add/(?P<id>\d+)$', views.add, name='add'),
    url(r'^user/(?P<id>\d+)$', views.user, name='user'),
]
