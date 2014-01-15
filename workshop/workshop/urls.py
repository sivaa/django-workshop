from django.conf.urls import patterns, include, url
from django.contrib import admin

from movies.views import movies, movies_remove, movies_edit


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^movies/$', movies),
    url(r'^movies/remove/(?P<movie_id>\d+)/$', movies_remove),
    url(r'^movies/edit/(?P<movie_id>\d+)/$', movies_edit),

    url(r'^admin/', include(admin.site.urls)),
)
