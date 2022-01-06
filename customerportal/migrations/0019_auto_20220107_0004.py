# Generated by Django 3.2.5 on 2022-01-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerportal', '0018_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='area',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='item',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]