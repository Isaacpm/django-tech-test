from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


#Model used to modify the default user profile, adding the phone number field
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)

#Model used to define the Business data
class Business(models.Model):
    BUSINESS_SECTORS = (
        ('RE','Retail'),
        ('PS','Professional Services'),
        ('FD','Food & Drink'),
        ('EN','Entertainment')
        )
    business_name = models.CharField(max_length=255)
    #The registered company number should be an 8 digits number, using a charfield with two validator as the numeric fields didn't have max_length
    registered_company_number = models.CharField(validators=[RegexValidator(regex='^[0-9]+$')],max_length=8)
    business_sector = models.CharField(choices=BUSINESS_SECTORS,max_length=21)
    user = models.ForeignKey(User)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField( max_length=1024)
    #Post code has a max of 9 characters
    post_code = models.CharField(max_length=9) 
    city_name = models.CharField(max_length=1024)

#Model used to define the Business data, assuming here a business could have more than one loan. So normalizing the loan information.
class Loan(models.Model):
    amount = models.PositiveIntegerField(validators=[MinValueValidator(10000),MaxValueValidator(100000)])
    number_of_days = models.PositiveIntegerField()
    reason = models.CharField(max_length=1024)
    user = models.ForeignKey(User)
    business = models.ForeignKey(Business)
