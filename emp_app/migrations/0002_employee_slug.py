# Generated by Django 3.2 on 2024-01-25 00:03

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='eid', unique=True),
            preserve_default=False,
        ),
    ]
