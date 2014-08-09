"""Models for the clients app.

The following tables will be contained within:
- Client
- Insurance
- Prescriptions
- Claims

"""
from django.db import models


class Client(models.Model):
    """Model of a client.

    A client will have the following fields:
    First Name
    Last Name
    Address
    Phone #
    Cell #
    Email
    Birthdate
    Gender
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
    phoneNumber = models.CharField(max_length=14, blank=True, default="")  # In the form of (780)-937-1514
    cellNumber = models.CharField(max_length=14, blank=True, default="")  # In the form of (780)-937-1514
    email = models.EmailField(max_length=254, blank=True, null=True)  # will cover all RFC3696/5321-compliant email addresses
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    credit = models.SmallIntegerField(default=0)
    notes = models.TextField(blank=True, default="")
    # insurance (foreign key)
    # dependants (foreign key)
    # Perscriptions (foreign key)
    # invoices (foreign key)
    # claims (foreign key)

    def __unicode__(self):
        return "%s - %s" % (self.firstName, self.lastName)

    def __str__(self):
        return self.__unicode__()

    def getAge(self):
        """Calculate clients age in years."""
        pass


class Perscription(models.Model):
    """Model of a saved perscription file.

    A perscription will have the following fields:
    Client
    Date added
    Prescription image

    """
    client = models.ForeignKey(Client)
    dateAdded = models.DateTimeField(auto_now_add=True)
    # TODO file field for uploading and saving the perscription, optional for now

    def __unicode__(self):
        clientName = self.client.firstName + " " + self.client.lastName
        date = self.dateAdded.date().isoformat()
        return "Perscription - %s - %s" % (clientName, date)

    def __str__(self):
        return self.__unicode__()


class Insurance(models.Model):
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
