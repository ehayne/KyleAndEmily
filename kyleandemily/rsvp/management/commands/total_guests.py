from django.core.management.base import BaseCommand, CommandError
from kyleandemily.rsvp.models import Invitation

class Command(BaseCommand):
    help = 'Prints the guest totals'

    def handle(self, *args, **options):
        welcome_guests = 0
        wedding_guests = 0
        farewell_guests = 0
        for inv in Invitation.objects.all():
            welcome_guests += inv.welcome_guests
            wedding_guests += inv.wedding_guests
            farewell_guests += inv.farewell_guests

        self.stdout.write('Total Welcome Dinner Guests: {0}'.format(welcome_guests))
        self.stdout.write('Total Wedding Guests: {0}'.format(wedding_guests))
        self.stdout.write('Total Farewell Brunch Guests: {0}'.format(farewell_guests))