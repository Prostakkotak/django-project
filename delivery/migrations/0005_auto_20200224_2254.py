# Generated by Django 3.0.1 on 2020-02-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_auto_20200224_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehisle',
            name='status',
        ),
        migrations.AddField(
            model_name='vehisle',
            name='can_be_booked',
            field=models.BooleanField(default=True),
        ),
    ]
