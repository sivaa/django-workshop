from django.conf.urls import patterns, include, url
from django.contrib import admin
from movies.views import movies, movies_remove

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^movies/$', movies),
    url(r'^movies/remove/(?P<movie_id>\d+)/$', movies_remove),

    url(r'^admin/', include(admin.site.urls)),
)
