# Generated by Django 3.1.7 on 2021-02-25 08:41

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaverequests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date.today)]),
        ),
    ]
