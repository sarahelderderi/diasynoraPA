# Generated by Django 3.0.6 on 2020-06-09 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0027_auto_20200609_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='volunteer',
            new_name='organiser',
        ),
    ]
