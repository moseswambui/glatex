# Generated by Django 3.2.5 on 2022-09-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('PAID', 'Paid'), ('NOT PAID', 'Not Paid')], default='Not Paid', max_length=50, null=True),
        ),
    ]
