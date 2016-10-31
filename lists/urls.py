from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'$', 'lists.views.home_page'),
    url(r'^index/$', 'lists.views.index_page'),
    url(r'^$', 'lists.views.home_page'),
    url(r'^add-task/$', 'lists.views.add_task'),
    url(r'^edit-task/(?P<task_id>[0-9]+)/$', 'lists.views.edit_task'),
    url(r'^delete-task/(?P<task_id>[0-9]+)/$', 'lists.views.delete_task'),
    url(r'^task-list/$', 'lists.views.task_list'),
]
