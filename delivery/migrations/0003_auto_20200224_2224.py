# Generated by Django 3.0.1 on 2020-02-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20200224_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehisle',
            name='delivery_method',
            field=models.CharField(blank=True, choices=[('g', 'ground'), ('a', 'air'), ('s', 'sea')], default='g', max_length=1),
        ),
        migrations.DeleteModel(
            name='DeliveryMethod',
        ),
    ]
