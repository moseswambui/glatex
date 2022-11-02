# Generated by Django 3.2.5 on 2022-10-20 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profiledetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiledetails',
            old_name='organisation',
            new_name='user_type',
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
