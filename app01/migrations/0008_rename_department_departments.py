# Generated by Django 4.1.7 on 2023-03-11 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='Departments',
        ),
    ]