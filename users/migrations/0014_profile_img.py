# Generated by Django 4.1.1 on 2022-10-12 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_image_illness_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='illness'),
        ),
    ]
