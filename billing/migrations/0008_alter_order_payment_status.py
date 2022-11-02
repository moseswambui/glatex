# Generated by Django 3.2.5 on 2022-09-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('PAID', 'PENDING'), ('PENDING', 'PENDING'), ('PARTIAL', 'PARTIAL')], default='PENDING', max_length=50),
        ),
    ]