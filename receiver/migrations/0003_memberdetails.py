# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0002_auto_20160804_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('has_payed', models.BooleanField()),
                ('pay_dt', models.DateTimeField(verbose_name=b'payment date')),
                ('member', models.ForeignKey(to='receiver.Member')),
            ],
        ),
    ]
