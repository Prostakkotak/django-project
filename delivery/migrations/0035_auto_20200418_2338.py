# Generated by Django 3.0.1 on 2020-04-18 20:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0034_auto_20200417_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 18, 23, 38, 23, 469804)),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 23, 38, 23, 467804), editable=False),
        ),
        migrations.CreateModel(
            name='ProposedNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_image', models.ImageField(default='none', upload_to='')),
                ('short_description', models.CharField(default='Description', max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 18, 23, 38, 23, 473806))),
                ('important_status', models.BooleanField(default=False, help_text='Are this news important or not')),
                ('views', models.IntegerField(default=0, editable=False)),
                ('tags', models.ManyToManyField(to='delivery.NewsTag')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ['-pub_date'],
            },
        ),
    ]
