# Generated by Django 2.2 on 2023-04-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='testimonial\\default.jpg', upload_to='testimonial/'),
        ),
    ]
