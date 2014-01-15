from django.conf.urls import patterns, include, url
from django.contrib import admin

from hello.views import hello, hello1, hello2, hello3


admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'workshop.views.home', name='home'),

    url(r'^hello/$', hello),
    url(r'^hello1/$', hello1),
    url(r'^hello2/$', hello2),
    url(r'^hello3/$', hello3),

    url(r'^admin/', include(admin.site.urls)),
)
