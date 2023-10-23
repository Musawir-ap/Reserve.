# Generated by Django 4.2.6 on 2023-10-22 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_subrole_main_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='sub_roles',
            field=models.ManyToManyField(default=None, editable=False, to='users.subrole'),
        ),
        migrations.AlterField(
            model_name='subrole',
            name='main_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subroles', to='users.role'),
        ),
    ]