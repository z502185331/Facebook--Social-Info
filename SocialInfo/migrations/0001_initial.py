# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('postTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SharedNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(default=-1)),
                ('next', models.ForeignKey(to='SocialInfo.SharedNode')),
            ],
        ),
        migrations.CreateModel(
            name='SharedReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('postTime', models.DateTimeField(auto_now_add=True)),
                ('referedPost', models.ForeignKey(to='SocialInfo.Post')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='sharedreference',
            name='user',
            field=models.ForeignKey(related_name='sharedPost', to='SocialInfo.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(related_name='post', to='SocialInfo.User'),
        ),
    ]
