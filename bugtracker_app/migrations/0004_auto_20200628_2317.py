# Generated by Django 3.0.6 on 2020-06-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0003_auto_20200616_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugticket',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
