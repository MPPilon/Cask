# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
                ('compensation', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='job',
            name='creatorUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='userList.User'),
        ),
        migrations.AddField(
            model_name='job',
            name='workerUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='userList.User'),
        ),
    ]
