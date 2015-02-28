from django.core.management.base import BaseCommand, CommandError
from kyleandemily.rsvp.models import Invitation

"""
first name 1,last name 1,first name 2,last name 2,first name 3,last name 3,first name 4,last name 4,household,side,address 1,city,state/country,postal code,email,phone

"""

class Command(BaseCommand):
    help = 'Prints the attending guests for import into other datastores'
    
    def handle(self, *args, **options):
        guest_count = 0
        families = []
        for inv in Invitation.objects.filter(responded=True):
            family = []
            for guest in inv.people.filter(attendingWedding=True):
                family.append(guest.first_name)
                family.append(guest.last_name)
                guest_count += 1
                
            
            family.append(inv.name)
            families.append(family)
                    
        
        for family in families:
            self.stdout.write(','.join(family))
        
        self.stdout.write("Total Guest Count: {0}".format(guest_count))