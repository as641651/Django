import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','exe2.settings')

import django
# Import settings
django.setup()

import random
from app2.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_email = fakegen.email()

        # Create new user Entry
        user_entry = User.objects.get_or_create(first_name=fake_name[0],last_name=fake_name[1],email=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
