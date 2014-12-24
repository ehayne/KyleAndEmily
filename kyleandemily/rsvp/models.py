'''Models for the RSVP application'''

from django.db import models

'''
TODO: possible ideas for models
add flag for +1 field for people whose date we don't know
add text field on invitation for general comments
remove dietary restriction

'''


class Invitation(models.Model):
    '''
Represents an invitation to the wedding
'''
# TODO: invitation name needs to be unique - i think the first name/last name combo also needs to be unique since it's the search key

    name = models.CharField(
        max_length=128,
        help_text='An informal name for this invitation'
    )
    comment = models.TextField(
        max_length=2000,
        blank=True
    )
    #TODO: remove song
    song = models.TextField(
        max_length=200,
        blank=True
    )
    helloGoodbyeInvite = models.BooleanField(
        default=False,
        help_text='Is this person invited to the welcome dinner and farewell lunch?'
    )
    plusOne = models.BooleanField(
        default=False,
        help_text='Does this invitation get a +1?'
    )
    responded = models.BooleanField(
        default=False,
        help_text='Has this invitation been responded to'
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    @property
    def guests(self):
        return self.people.filter(attendingWedding=True).count()


class Person(models.Model):
    '''
Represents a person coming to the wedding
'''
    invitation = models.ForeignKey(
        Invitation,
        related_name='people'
    )
    first_name = models.CharField(
        max_length=64,
        blank=True
    )
    last_name = models.CharField(
        max_length=128,
        blank=True
    )
    attendingWedding = models.NullBooleanField(
        blank=True,
        null=True
    )
    attendingWelcome = models.NullBooleanField(
        blank=True,
        null=True
    )
    attendingFarewell = models.NullBooleanField(
        blank=True,
        null=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )