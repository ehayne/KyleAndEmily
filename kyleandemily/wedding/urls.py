from django.conf.urls import patterns, url, include

import kyleandemily.wedding.views as wedding_views

urlpatterns = patterns(
    '',
    url(r'^$',
    	wedding_views.home,
    	name='home'),
    url(r'^(?i)about_us/$',
    	wedding_views.about,
    	name='about'),
    url(r'^(?i)gallery/$',
    	wedding_views.gallery,
    	name='gallery'),
    url(r'^(?i)details/$',
    	wedding_views.details,
    	name='wedding_details'),
    url(r'^(?i)hotels/$',
    	wedding_views.hotels,
    	name='hotel_info'),
    url(r'^(?i)rsvp/', include('kyleandemily.rsvp.urls')),
    url(r'^(?i)registry/$',
    	wedding_views.registry,
    	name='registry'),
)
