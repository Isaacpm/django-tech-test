"""
Loans application Models file, describes the data models used by the loan, and frontend applications
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


#Model used to modify the default user profile, adding the phone number field
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
"""
Model used to define the Business data
Adding the address as part of the business model was considered as a business should have only one address,
and it's unlikely that different business will share the exact same address, even if being in the same building.
City and post code may have been normalized but seemed an overkill for two small pieces of text.
"""
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
    #We want to return the business name to make a better display of information in the admin and input forms
    def __unicode__(self):
       return self.business_name

#Model used to define the Loan data, assuming a business could have more than one loan. So normalizing the loan information.
class Loan(models.Model):
    amount = models.PositiveIntegerField(validators=[MinValueValidator(10000),MaxValueValidator(100000)])
    number_of_days = models.PositiveIntegerField()
    reason = models.CharField(max_length=1024)
    user = models.ForeignKey(User)
    business_name = models.ForeignKey(Business)
    #The reason seemed to be the more appropiate field to return in order to identify loans, a combination of more fields could be used but it may difficult the presentation of the information
    def __unicode__(self):
       return self.reason
