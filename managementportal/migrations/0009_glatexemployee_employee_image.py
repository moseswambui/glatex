# Generated by Django 3.2.5 on 2021-08-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0008_screenprintingsales_client_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='glatexemployee',
            name='Employee_image',
            field=models.ImageField(blank=True, null=True, upload_to='employeephotos'),
        ),
    ]
