# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0004_auto_20160808_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='amount',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
