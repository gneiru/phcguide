# Generated by Django 4.1.1 on 2022-11-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_delete_dietschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illness',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
