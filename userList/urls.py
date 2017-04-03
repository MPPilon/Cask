from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from userList import views
from userList.views import ListCreateUsers

urlpatterns = [
    # /userlist/
    url(r'^$', views.index, name='index'),
    # /userlist/api/125
    url(r'^api/(?P<user_id>[0-9]+)', views.detail, name='detail'),
    url(r'^api/users', ListCreateUsers.as_view(), name='list_users'),
]

urlpatterns = format_suffix_patterns(urlpatterns)