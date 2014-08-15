#!/usr/bin/env python
import os
import datetime
from django.utils import timezone


def populate():
    # Constants for the client model
    MALE = Client.GENDER_CHOICES[0][0]
    FEMALE = Client.GENDER_CHOICES[1][0]
    # Constants for claim model
    CASH = Claim.PAYMENT_CHOICES[0][0]
    # Add/create models here
    eric = add_client("Eric", "Klinger", "11408 44 ave", datetime.date(1988, 12, 30), MALE)
    chris = add_client("Chris", "Klinger", "11408 44 ave", datetime.date(1991, 6, 14), MALE)
    jay = add_client("Jason", "Mu", "4077 69ave", datetime.date(1980, 6, 14), MALE)
    dan = add_client("Danny", "Mu", "13499 70ave", datetime.date(1983, 8, 14), MALE)
    cloney = add_client("Cloney", "McStudent", "12345 42 ave", datetime.date(1993, 5, 22), MALE)
    jane = add_client("Jane", "Doe", "2943 69 ave", datetime.date(1985, 12, 8), FEMALE)
    john = add_client("John", "Doe", "2943 69 ave", datetime.date(1984, 8, 20), MALE)
    add_perscription(eric, timezone.now())
    add_perscription(eric, timezone.now())
    add_perscription(chris, timezone.now())
    add_perscription(chris, timezone.now())
    add_perscription(jay, timezone.now())
    add_perscription(jay, timezone.now())
    add_perscription(dan, timezone.now())
    add_perscription(dan, timezone.now())
    add_perscription(cloney, timezone.now())
    add_perscription(jane, timezone.now())
    add_perscription(john, timezone.now())
    eric_insurance = add_insurance(eric, "Some_provider", "PN9999", "CN9999", 50)
    chris_insurance = add_insurance(chris, "Some_provider", "PN9998", "CN9998", 50)
    jay_insurance = add_insurance(jay, "Some_provider", "PN9997", "CN9997", 50)
    dan_insurance = add_insurance(dan, "Some_provider", "PN9996", "CN9996", 50)
    cloney_insurance = add_insurance(cloney, "Some_provider", "PN9995", "CN9995", 50)
    jane_insurance = add_insurance(jane, "Some_provider", "PN9994", "CN9994", 50)
    john_insurance = add_insurance(john, "Some_provider", "PN9994", "CN9994", 50)
    add_claim(eric, eric_insurance, timezone.now(), CASH)
    add_claim(chris, chris_insurance, timezone.now(), CASH)
    add_claim(jay, jay_insurance, timezone.now(), CASH)
    add_claim(dan, dan_insurance, timezone.now(), CASH)
    add_claim(cloney, cloney_insurance, timezone.now(), CASH)
    add_claim(jane, jane_insurance, timezone.now(), CASH)
    add_claim(john, john_insurance, timezone.now(), CASH)

    # Add admin users
    # Have to hash passwords so get_or_create will work
    password = hashers.make_password("admin")
    add_admin("admin", password)
    add_admin("jay", password)
    add_admin("dan", password)
    add_admin("eric", password)
    add_admin("chris", password)


def add_model_example():
    # use <model>.objects.get_or_create here and take the 0th index [0]
    pass


def add_admin(username, password):
    a = User.objects.get_or_create(username=username,
                                   password=password,
                                   is_staff=True,
                                   is_superuser=True)
    return a[0]


def add_client(firstName, lastName, address, birthdate, gender):
    c = Client.objects.get_or_create(firstName=firstName,
                                     lastName=lastName,
                                     address=address,
                                     birthdate=birthdate,
                                     gender=gender)
    return c[0]


def add_perscription(client, dateAdded):
    p = Perscription.objects.get_or_create(client=client,
                                           dateAdded=dateAdded)
    return p[0]


def add_insurance(client, provider, policyNumber, contractNumber, coveragePercent):
    i = Insurance.objects.get_or_create(client=client,
                                        provider=provider,
                                        policyNumber=policyNumber,
                                        contractNumber=contractNumber,
                                        coveragePercent=coveragePercent)
    return i[0]


def add_claim(client, insurance, submittedDate, paymentType):
    c = Claim.objects.get_or_create(client=client,
                                    insurance=insurance,
                                    submittedDate=submittedDate,
                                    paymentType=paymentType)
    return c[0]


# Start execution here!
if __name__ == '__main__':
    print "Starting database population script"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orthotics_project.settings')
    # from app.models import <model>, <model>
    from django.contrib.auth.models import User
    import django.contrib.auth.hashers as hashers
    from clients.models import Client, Perscription, Insurance, Claim, Dependant
    populate()
    print "Done populating database"
