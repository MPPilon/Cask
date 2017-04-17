from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from userList import views

urlpatterns = [
    # /userlist/
    # url(r'^$',
    #   views.index,
    #   name='index'),


    # /userlist/api/users/<user_id>
    url(r'^api/users/(?P<user_id>[0-9]+)',
        views.UserDetails.as_view(),
        name='user_details'),

    # /userlist/api/users
    url(r'^api/users',
        views.UserList.as_view(),
        name='user_list'),

    url(r'^jobList/',
        views.JobList.as_view(),
        name='job_list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)