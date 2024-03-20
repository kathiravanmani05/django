
# forms.py
from django import forms
from .models import ScrapedData

class ScrapedDataForm(forms.ModelForm):
    class Meta:
        model = ScrapedData
        fields = ['address', 'city', 'state', 'zip', 'acreage', 'market_value', 'assessed_value', 'offer_amount', 'tax_due', 'email', 'phone_number', 'comment']
