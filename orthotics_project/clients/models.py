"""Models for the clients app

The following tables will be contained within:
- Client
- Prescriptions
- Insurance
- Claims

"""

from django.db import models

"""
Table: Client
Fields:
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
Husband and Wife’s coverage (there could be multiple policies)
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
Reports:
1) Outstanding Payments
- 15/30/60/90 day cycle (insurance company “Direct billing”/patient “Non-direct billing”)
- Paid claims 15/30/60/90 days (or possibly if we can have a have a calendar where we can pick from a specific start date to and end date)
2) Paid claims 15/30/60/90 days (or possibly if we can have a have a calendar where we can pick from a specific start date to and end date)
3) Monthly breakdown of revenue
    - amount invoiced, amount expected, amount actually paid (possibly a graph, or a table)
"""
