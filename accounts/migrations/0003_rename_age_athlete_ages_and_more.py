# Generated by Django 5.0.6 on 2024-08-16 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_athlete_sport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete',
            old_name='age',
            new_name='ages',
        ),
        migrations.RenameField(
            model_name='athlete',
            old_name='gender',
            new_name='genders',
        ),
        migrations.RenameField(
            model_name='athlete',
            old_name='sport',
            new_name='sports',
        ),
    ]
