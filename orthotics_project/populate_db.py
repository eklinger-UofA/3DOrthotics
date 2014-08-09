#!/usr/bin/env python
import os
import datetime

def populate():
    # Add/create models here
    MALE = Client.GENDER_CHOICES[0][0]
    FEMALE = Client.GENDER_CHOICES[1][0]
    add_client("Eric", "Klinger", "11408 44 ave", datetime.date(1988, 12, 30), MALE)
    add_client("Chris", "Klinger", "11408 44 ave", datetime.date(1991, 6, 14), MALE)

def add_model():
    # use object.get_or_create here and take the 0th index [0]
    pass

def add_client(firstName, lastName, address, birthdate, gender):
    c = Client.objects.get_or_create(firstName=firstName,
                                     lastName=lastName,
                                     address=address,
                                     birthdate=birthdate,
                                     gender=gender)

# Start execution here!
if __name__ == '__main__':
    print "Starting database population script"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orthotics_project.settings')
    # from app.models import <model>, <model>
    from clients.models import Client
    populate()
