from django.conf import settings
from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf.urls.static import static


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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'views.404error'
# handler500 = 'views.500error'