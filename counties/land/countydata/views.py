import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from .models import ScrapedData
from django.views.decorators.http import require_POST
from . forms import ScrapedDataForm

def home(request):
    scraped_data = ScrapedData.objects.all()       
    return render(request, 'home.html', {'scraped_data': scraped_data})

def apn_details(request, apn):
    # Logic to fetch additional details based on the APN
    # You can retrieve the details from the database or any other source
    # For demonstration purposes, let's assume you have a model named Property with APN as one of its fields
    # You can replace this with your actual model and logic
    property_details = get_object_or_404(ScrapedData, APN=apn)
    property_details.refresh_from_db()
    
    print(property_details)
    
    return render(request, 'property_details.html', {'property_details': property_details})

def update_property_details(request, apn):
    property_details = get_object_or_404(ScrapedData, APN=apn)
    if request.method == 'POST':
        form = ScrapedDataForm(request.POST, instance=property_details)
        if form.is_valid():
            form.save()
            return redirect('apn_details', apn=apn)  # Redirect to the correct view name
    else:
        form = ScrapedDataForm(instance=property_details)
    return render(request, 'update_property_details.html', {'form': form})


