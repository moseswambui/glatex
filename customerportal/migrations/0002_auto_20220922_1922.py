# Generated by Django 3.2.5 on 2022-09-22 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20220922_1922'),
        ('customerportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
