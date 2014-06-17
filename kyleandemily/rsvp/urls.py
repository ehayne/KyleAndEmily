from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

import kyleandemily.rsvp.views as rsvp_views

urlpatterns = patterns(
    '',

    url(r'^.admin/', include(admin.site.urls)),

    url(r'^lookup/$',
        rsvp_views.lookup,
        name='lookup'),
    url(r'^save/$',
        rsvp_views.save,
        name='save'),
    url(r'',
        rsvp_views.landing,
        name='landing'),
    url(r'^(?P<first_name>[a-zA-Z]+)/$',
        rsvp_views.landing,
        name='landing'),
)