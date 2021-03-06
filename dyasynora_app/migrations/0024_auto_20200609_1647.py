# Generated by Django 3.0.6 on 2020-06-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0023_auto_20200606_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=29, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='org',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='org_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
