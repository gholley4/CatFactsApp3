# Generated by Django 4.1.4 on 2022-12-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_fact_likes_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
