# Generated by Django 4.2.6 on 2023-11-02 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tokenapp', '0003_auto_20231102_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='assigned_staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tokens_assigned_to_staff', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='token',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='tokens_with_status', to='tokenapp.status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='status_history',
            field=models.ManyToManyField(related_name='tokens_in_status_history', through='tokenapp.StatusHistory', to='tokenapp.status'),
        ),
        migrations.AlterField(
            model_name='token',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tokens_for_purpose', to='tokenapp.purpose'),
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tokens_created_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]