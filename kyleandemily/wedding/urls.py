from django.conf.urls import patterns, url, include

import kyleandemily.wedding.views as wedding_views

urlpatterns = patterns(
    '',
    url(r'^$',
    	wedding_views.about,
    	name='about_us'),
    url(r'^gallery/$',
    	wedding_views.gallery,
    	name='gallery'),
    url(r'^details/$',
    	wedding_views.details,
    	name='wedding_details'),
    url(r'^hotels/$',
    	wedding_views.hotels,
    	name='hotel_info'),
    url(r'^rsvp/', include('kyleandemily.rsvp.urls')),
    url(r'^registry/$',
    	wedding_views.registry,
    	name='registry'),
)
