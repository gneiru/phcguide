# Generated by Django 4.1.2 on 2022-11-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_illness_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietplan',
            name='classification',
            field=models.CharField(choices=[('underweight', 'UNDERWEIGHT'), ('overweight', 'OVERWEIGHT'), ('obese', 'OBESE'), ('normal', 'NORMAL'), ('xobese', 'EXTREMELY OBESE')], default='normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='dietsupplement',
            name='classification',
            field=models.CharField(choices=[('underweight', 'UNDERWEIGHT'), ('overweight', 'OVERWEIGHT'), ('obese', 'OBESE'), ('normal', 'NORMAL'), ('xobese', 'EXTREMELY OBESE')], default='normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='physicalactivities',
            name='classification',
            field=models.CharField(choices=[('underweight', 'UNDERWEIGHT'), ('overweight', 'OVERWEIGHT'), ('obese', 'OBESE'), ('normal', 'NORMAL'), ('xobese', 'EXTREMELY OBESE')], default='normal', max_length=50),
        ),
    ]
