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
    name = models.CharField(
        max_length=128,
        help_text='An informal name for this invitation'
    )
    comment = models.TextField(
        # max_length = 2000, TODO: do we want max length?
        blank=True
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
        return self.people.filter(attending=True).count()


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
    attending = models.NullBooleanField(
        blank=True,
        null=True
    )
    has_plus_one = models.BooleanField(
        default=False,
        help_text='Does this person have an unnamed +1?'
    )
    updated = models.DateTimeField(
        auto_now=True
    )