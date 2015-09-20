# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'id')),
                ('name', models.CharField(max_length=255, db_column=b'name')),
                ('role', models.CharField(max_length=255, db_column=b'role')),
                ('division', models.CharField(max_length=255, db_column=b'division')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'id')),
                ('course_name', models.CharField(max_length=255, db_column=b'course_name')),
                ('subject_name', models.CharField(max_length=255, db_column=b'subject_name')),
                ('grade', models.IntegerField(db_column=b'grade')),
                ('standard', models.IntegerField(db_column=b'standard')),
            ],
        ),
    ]
