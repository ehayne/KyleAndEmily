from django.conf import settings
from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

import kyleandemily.views as views

urlpatterns = patterns(
    '',
    # url(r'^$',
    #        views.under_construction,
    #        name='under_construction'),
    url(r'^', include('kyleandemily.wedding.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?i)wedding/', include('kyleandemily.wedding.urls')),
    url(r'^(?i)photologue/', include('photologue.urls')),
)   

if settings.APP_ENV == 'local':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'views.404error'
# handler500 = 'views.500error'
