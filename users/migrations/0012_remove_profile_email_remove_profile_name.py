# Generated by Django 4.1.1 on 2022-10-11 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_profile_email_profile_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
