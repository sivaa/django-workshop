from django.conf.urls import patterns, include, url
from django.contrib import admin

from todo.views import tasks, tasks_remove, tasks_edit, tasks_priority_high, \
    tasks_priority_low, tasks_completed, tasks_not_completed, tasks_overdue, \
    tasks_due_today


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^tasks/$', tasks),
    url(r'^tasks/remove/(?P<task_id>\d+)/$', tasks_remove),
    url(r'^tasks/edit/(?P<task_id>\d+)/$', tasks_edit),
    url(r'^tasks/priority/high/$', tasks_priority_high),
    url(r'^tasks/priority/low/$', tasks_priority_low),
    url(r'^tasks/duetoday/$', tasks_due_today),
    url(r'^tasks/overdue/$', tasks_overdue),
    url(r'^tasks/completed/$', tasks_completed),
    url(r'^tasks/notcompleted/$', tasks_not_completed),

    ('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


from django.contrib.auth import views as auth_views
