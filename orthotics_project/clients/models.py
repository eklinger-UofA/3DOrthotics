"""Models for the clients app.

The following tables will be contained within:
- Client
- Prescriptions
- Insurance
- Claims

"""
from django.db import models


class Client(models.Model):
    """Model of a client in our system

    A client will have the following fields:
    First Name
    Last Name
    Address
    Phone #
    Cell #
    Email
    Birthdate
    Credit (current credit from insurance company)
    Notes (for log of communication)
    Dependants - another table
    Prescriptions - another table
    Insurance - another table
    """
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'),
                      (FEMALE, 'Female'))

    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    # TODO Write validators for the phone numbers below
    phoneNumber = models.CharField(max_length=14, blank=True, null=True)  # In the form of (780)-937-1514
    cellNumber = models.CharField(max_length=14, blank=True, null=True)  # In the form of (780)-937-1514
    email = models.EmailField(max_length=254, blank=True, null=True)  # will cover all RFC3696/5321-compliant email addresses
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    credit = models.SmallIntegerField(default=0)
    # insurance (foreign key)
    # dependants (foreign key)
    # Perscriptions (foreign key)
    # invoices (foreign key)
    # claims (foreign key)

    def __unicode__(self):
        return self.firstName + " - " + self.lastName

    def __str__(self):
        return self.__unicode__()

    def getAge(self):
        """Calculate clients age in years."""
        pass

    """
    Table Prescriptions:
    Fields:
    Client
    Date scanned
    Prescription image
    """

    """
    Table: Insurance
    Fields:
    Husband and Wifes coverage (there could be multiple policies)
    Provider
    Policy #
    Contract #
    coverage %
    Benefit year (when the insurers benefit period renews):
    1) Calendar Year (Jan 1)
    2) could be a specific month in the year
    Example: April 1

    Direct/indirect billing
    coverage conditions
    """


    """
    Table: Claims
    Fields:
    Submitted date
    invoice date
    paid date
    client/dependant
    insurance
    amount claimed
    expected back
    payment type (cash, cheque, credit)
    Look up report types from google docs
    """



