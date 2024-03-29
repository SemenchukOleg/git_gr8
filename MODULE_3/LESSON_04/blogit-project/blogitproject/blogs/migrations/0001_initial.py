# Generated by Django 3.2.18 on 2023-04-17 17:43

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('Travel', 'Travel'), ('Lifestyle', 'Lifestyle'), ('Cooking', 'Cooking'), ('Science', 'Science'), ('Tech', 'Tech'), ('Sport', 'Sport'), ('Movie', 'Movie'), ('Art', 'Art'), ('Other', 'Other')], default='Other', max_length=15)),
                ('text_slug', models.CharField(blank=True, default='', max_length=200)),
                ('slug', models.CharField(blank=True, default='', max_length=160)),
                ('image', models.ImageField(upload_to='blog_images/%Y/%m/%d', verbose_name='Blog image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('likes', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, help_text='Collects profile ids as Integer', size=None)),
                ('is_published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('comments', models.ManyToManyField(blank=True, to='comments.Comment')),
            ],
        ),
    ]
