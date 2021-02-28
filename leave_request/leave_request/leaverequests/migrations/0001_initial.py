# Generated by Django 3.1.7 on 2021-02-25 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20210225_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.TextField(blank=True, null=True)),
                ('reason', models.CharField(choices=[('Sick', 'Sick'), ('Family Reasons', 'Family Reasons'), ('Personal Leave', 'Personal Leave'), ('Leave without pay', 'Leave without pay'), ('Other', 'Other')], default='Sick', max_length=20)),
                ('approved', models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('pending', 'pending')], default='Sick', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaverequest', to='users.profile')),
            ],
        ),
    ]
