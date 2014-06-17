from django.conf.urls import patterns, url

import kyleandemily.wedding.views as wedding_views
import kyleandemily.rsvp.views as rsvp_views

urlpatterns = patterns(
    '',
    url(r'^$',
    	wedding_views.home,
    	name='about_us'),
    url(r'^about/$',
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
    url(r'^rsvp/$',
    	rsvp_views.lookup,
    	name='rsvp'),
    url(r'^registry/$',
    	wedding_views.registry,
    	name='registry'),
)
