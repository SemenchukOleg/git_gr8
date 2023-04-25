# Generated by Django 3.2.18 on 2023-04-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog_images/%Y/%m/%d', verbose_name='Blog image'),
        ),
    ]