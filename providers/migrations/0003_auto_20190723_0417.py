# Generated by Django 2.2.3 on 2019-07-23 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20190723_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
