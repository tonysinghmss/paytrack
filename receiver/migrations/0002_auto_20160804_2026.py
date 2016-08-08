# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Member',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='member_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='member_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='team_members',
            new_name='members',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='team_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teammember',
            old_name='user',
            new_name='member',
        ),
    ]
