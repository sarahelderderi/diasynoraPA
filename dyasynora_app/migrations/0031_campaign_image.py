# Generated by Django 3.0.6 on 2020-06-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0030_campaign_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='image',
            field=models.ImageField(default='default_proj.jpg', upload_to='project_pics'),
        ),
    ]
