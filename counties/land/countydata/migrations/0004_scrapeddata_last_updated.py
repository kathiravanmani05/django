# Generated by Django 5.0.2 on 2024-03-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countydata', '0003_scrapeddata_offer_amount_scrapeddata_tax_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapeddata',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
