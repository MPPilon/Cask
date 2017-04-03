from django.conf.urls import include, url

from . import views

urlpatterns = [
    # /userlist/
    url(r'^$', views.index, name='index'),
    # /userlist/125
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
]