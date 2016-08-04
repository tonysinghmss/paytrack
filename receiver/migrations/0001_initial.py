# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.ForeignKey(to='receiver.Team')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")])),
                ('member_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(to='receiver.User'),
        ),
        migrations.AddField(
            model_name='team',
            name='team_members',
            field=models.ManyToManyField(to='receiver.User', through='receiver.TeamMember'),
        ),
    ]
