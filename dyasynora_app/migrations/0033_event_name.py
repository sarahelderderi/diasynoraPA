# Generated by Django 3.0.6 on 2020-06-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0032_campaign_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='event name', max_length=50),
            preserve_default=False,
        ),
    ]