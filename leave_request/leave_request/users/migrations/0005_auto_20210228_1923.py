# Generated by Django 3.0.11 on 2021-02-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210228_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='leave_balances',
            field=models.PositiveIntegerField(default=30),
        ),
    ]