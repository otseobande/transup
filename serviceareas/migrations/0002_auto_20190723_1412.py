# Generated by Django 2.2.3 on 2019-07-23 14:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='coordinates',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=6, max_digits=9), size=None), size=None),
        ),
    ]