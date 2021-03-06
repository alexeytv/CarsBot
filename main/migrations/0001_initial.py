# Generated by Django 3.0.2 on 2020-01-22 20:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=10)),
                ('vin', models.CharField(max_length=17)),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('address', models.CharField(max_length=512)),
                ('geo', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('status', models.TextField(choices=[('ACTIVE', 'Active'), ('HIDDEN', 'Hidden'), ('DELETED', 'Deleted')], default='ACTIVE')),
                ('comments', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField()),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.IntegerField()),
                ('is_success', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TelegramUser')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='image', to='main.Car')),
            ],
        ),
    ]
