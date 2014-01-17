from django.conf.urls import patterns, include, url
from django.contrib import admin

from todo.views import tasks, tasks_remove, tasks_edit


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^tasks/$', tasks),
    url(r'^tasks/remove/(?P<task_id>\d+)/$', tasks_remove),
    url(r'^tasks/edit/(?P<task_id>\d+)/$', tasks_edit),

    url(r'^admin/', include(admin.site.urls)),
)
