from django.conf.urls import patterns, include, url
from django.contrib import admin
# from movies.views import movies

admin.autodiscover()

urlpatterns = patterns('',

#    url(r'^movies/$', movies),

    url(r'^admin/', include(admin.site.urls)),
)
