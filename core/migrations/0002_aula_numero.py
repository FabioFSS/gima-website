# Generated by Django 4.0.4 on 2022-06-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]
