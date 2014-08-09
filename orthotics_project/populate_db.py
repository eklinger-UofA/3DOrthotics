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
    add_client("Chris", "Klinger", "11408 44 ave", datetime.date(1991, 6, 14), MALE)
    add_client("Jason", "Mu", "4077 69ave", datetime.date(1980, 6, 14), MALE)
    add_client("Danny", "Mu", "13499 70ave", datetime.date(1983, 8, 14), MALE)
    add_perscription(eric, timezone.now())
    eric_insurance = add_insurance(eric, "Some_provider", "PN9999", "CN9999", 50)
    add_claim(eric, eric_insurance, timezone.now(), CASH)


def add_model_example():
    # use <model>.objects.get_or_create here and take the 0th index [0]
    pass


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
    from clients.models import Client, Perscription, Insurance, Claim
    populate()
    print "Done populating database"
