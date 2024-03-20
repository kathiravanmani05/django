from django import forms
from .models import ScrapedData

from django import forms
from .models import ScrapedData  # Import your model here

class ScrapedDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = 'test@test.com'  # Set initial value for email field
        for field in self.fields.values():
            field.required = False

    class Meta:
        model = ScrapedData
        fields = ['owner_name', 'address', 'city', 'state', 'zip', 'acreage', 'market_value', 'assessed_value', 'offer_amount', 'tax_due', 'email', 'phone_number', 'comment']
        widgets = {
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'zip': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'acreage': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'market_value': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'assessed_value': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'offer_amount': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'tax_due': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
        }

