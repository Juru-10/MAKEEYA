# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-19 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0002_item_today_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_identification_number', models.CharField(max_length=100)),
                ('prefered_username', models.CharField(max_length=100)),
                ('business_phone_number', models.IntegerField()),
                ('business_email', models.EmailField(max_length=254)),
                ('Business_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='item_name',
        ),
        migrations.AddField(
            model_name='buyer',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyer',
            name='first_name',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyer',
            name='last_name',
            field=models.CharField(default=3, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
