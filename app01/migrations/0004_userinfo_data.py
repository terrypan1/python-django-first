# Generated by Django 4.1.7 on 2023-03-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_delete_department_delete_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='data',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
