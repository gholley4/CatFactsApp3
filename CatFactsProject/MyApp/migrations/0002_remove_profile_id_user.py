# Generated by Django 4.1.4 on 2022-12-23 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]
