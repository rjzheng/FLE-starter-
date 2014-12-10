from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', 'json_read'),
    url(r'^admin/', include(admin.site.urls)),
)
