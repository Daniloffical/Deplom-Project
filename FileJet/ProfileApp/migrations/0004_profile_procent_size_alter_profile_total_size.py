# Generated by Django 4.1.7 on 2023-06-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0003_profile_total_size_profile_used_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='procent_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_size',
            field=models.IntegerField(default=104857600),
        ),
    ]
