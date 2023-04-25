# Generated by Django 3.2.18 on 2023-04-19 17:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20230419_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, help_text='Collects profile ids as Integer', size=None),
        ),
    ]
