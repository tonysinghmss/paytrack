# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0003_memberdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MemberDetails',
            new_name='MemberPaymentDetails',
        ),
    ]
