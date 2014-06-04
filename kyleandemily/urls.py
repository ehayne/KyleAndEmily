from django.conf.urls import patterns, include, url, handler404, handler500

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
    url(r'^photologue/', include('photologue.urls')),
)

# handler404 = 'views.404error'
# handler500 = 'views.500error'
