# Generated by Django 4.1.1 on 2022-11-05 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_physicalactivities_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DietSchedule',
        ),
    ]
