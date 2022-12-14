# Generated by Django 3.2.5 on 2022-09-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('PAID', 'PAID'), ('PENDING', 'PENDING'), ('PARTIAL', 'PARTIAL')], default='PENDING', max_length=50),
        ),
    ]
