# Generated by Django 4.2.6 on 2023-10-24 07:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0015_remove_staffprofile_baseprofile_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('baseprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='users.baseprofile')),
                ('staff_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=25)),
                ('qualifications', models.TextField(blank=True, max_length=200, null=True)),
            ],
            bases=('users.baseprofile',),
        ),
    ]
