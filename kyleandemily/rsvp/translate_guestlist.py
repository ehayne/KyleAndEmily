import json
DB = []

PERSON_COUNT = 0
def split_name(guest_info):
    return guest_info.split()

def add_guest(guest_info, invitation_count):
    global PERSON_COUNT, DB
    PERSON_COUNT += 1
    first_name, last_name = split_name(guest_info)
    
    person_fields = {
        'invitation': invitation_count,
        'first_name': first_name,
        'last_name': last_name,
        'updated': "2015-01-09T23:51:37.745Z"
    }
    person_document = {
        'pk': PERSON_COUNT,
        'model': 'rsvp.person',
        'fields': person_fields
    }
    DB.append(person_document)


with open('./guestlist.csv','r') as fh:
    data = fh.read().splitlines()[1:-4]
    
invitation_count = 0
for line in data:
    invitation_count += 1
    invitation_name, guest1, guest2, child1, child2, child3, child4, _, invitation_out_of_town, invitation_plus_one = line.split(',')
    add_guest(guest1, invitation_count)
    if guest2:
        add_guest(guest2, invitation_count)
    if child1:
        add_guest(child1, invitation_count)
    if child2:
        add_guest(child2, invitation_count)
    if child3:
        add_guest(child3, invitation_count)
    if child4:
        add_guest(child4, invitation_count)
    
    invitation_fields = {
        'name': invitation_name,
        'helloGoodbyeInvite': invitation_out_of_town == 'Y',
        'plusOne': invitation_plus_one == 'Y',
        'updated': "2015-01-09T23:51:37.745Z"
    }
    invitation_document = {
        'pk': invitation_count,
        'model': 'rsvp.invitation',
        'fields': invitation_fields
    }
    DB.append(invitation_document)

    with open('./fixtures/guestlist.json', 'w') as json_fh:
        json_fh.write(json.dumps(DB, indent=4, sort_keys=True))