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

    # POST call: Creates a job
    # /jobList/post
    url(r'^jobList/post',
        views.JobList.as_view(),
        name='job_list_create'),

    # DELETE call: Deletes a job
    # /jobList/delete/<key>
    url(r'^jobList/delete/(?P<key>[0-9]+)',
        views.JobList.as_view(),
        name='job_list_delete'),

    # PUT call: Edit a particular job
    # /jobList/edit/<key>
    url(r'^jobList/edit/(?P<key>[0-9]+)',
        views.JobList.as_view(),
        name='job_list_edit'),

    # GET call: Gets the full job list
    # /jobList/
    url(r'^jobList/',
        views.JobList.as_view(),
        name='job_list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)