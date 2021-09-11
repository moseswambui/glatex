# Generated by Django 3.2.5 on 2021-09-11 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managementportal', '0020_rename_cloth_category_town_clothingexpenses_item_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='town_clothingexpenses',
            old_name='Cloth_Quantity',
            new_name='Cost_Per_Item',
        ),
        migrations.RenameField(
            model_name='town_clothingexpenses',
            old_name='Cloth_Color',
            new_name='Item_Color',
        ),
        migrations.RenameField(
            model_name='town_clothingexpenses',
            old_name='Cost_Per_Cloth',
            new_name='Item_Quantity',
        ),
        migrations.RenameField(
            model_name='town_clothingexpenses',
            old_name='Cloth_Size',
            new_name='Item_Size',
        ),
        migrations.RenameField(
            model_name='town_clothingexpenses',
            old_name='Cloth_Type',
            new_name='Item_Type',
        ),
    ]
