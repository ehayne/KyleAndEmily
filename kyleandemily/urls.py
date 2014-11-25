from django.conf import settings
from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView


from django.contrib import admin
admin.autodiscover()

import kyleandemily.views as views

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('^wedding/'), permanent=False), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wedding/', include('kyleandemily.wedding.urls')),
    url(r'^photologue/', include('photologue.urls')),
)   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'views.404error'
# handler500 = 'views.500error'
