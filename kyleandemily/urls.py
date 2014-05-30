from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import kyleandemily.views as views
import kyleandemily.wedding.urls

urlpatterns = patterns('',
   url(r'^$',
       views.under_construction,
       name='under_construction'),
#    url(r'^$', include('kyleandemily.wedding.urls')),  # change in the future if we change site
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wedding/', include('kyleandemily.wedding.urls')),
)
