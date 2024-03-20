
from django.contrib import admin
from django.urls import path, include
from countydata import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # Include Django's built-in authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name = 'home'),
    path('details/<str:apn>/', views.apn_details, name='apn_details'),
    path('edit/<str:apn>/', views.edit_scraped_data, name='edit_scraped_data'),
]
