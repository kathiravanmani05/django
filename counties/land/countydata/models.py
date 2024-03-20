from django.db import models
from accounts.models import User

class ScrapedData(models.Model):

    APN = models.CharField(max_length=50, primary_key=True)
    owner_name = models.CharField(max_length=255, null = False)
    Property_State = models.CharField(max_length=5, null = False)
    Property_County = models.CharField(max_length=25, null = False)
    address = models.TextField()
    city = models.CharField(max_length=100, null = False , default='')
    state = models.CharField(max_length=10, null = False, default='')
    zip = models.CharField(max_length=15, null = False, default='')
    acreage = models.CharField(max_length=25,null = True)
    improvement_homesite_value = models.CharField(max_length=25, null = True)
    improvement_non_Homesite_value = models.CharField(max_length=25, null = True)
    land_homesite_value = models.CharField(max_length=25, null = True)
    land_non_homesite_value = models.CharField(max_length=25, null = True)
    agricultural_market_valuation = models.CharField(max_length=25,null = True)
    assessed_value = models.CharField(max_length=25,null = True)
    market_value = models.CharField(max_length=25, null = True)
    email = models.CharField(max_length=250, null = True ,default='')
    phone_number = models.CharField(max_length=150, null = True , default='')
    comment = models.TextField(default='')
    offer_amount = models.CharField(max_length=25,null = True, default='')
    tax_due = models.CharField(max_length=25,null = True, default='')
    last_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)




