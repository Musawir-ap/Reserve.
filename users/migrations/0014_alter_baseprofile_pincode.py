# Generated by Django 4.2.6 on 2023-10-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_baseprofile_clientprofile_staffprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprofile',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]