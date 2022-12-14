# Generated by Django 4.1.1 on 2022-10-25 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0016_alter_dietplan_name_alter_dietsupplement_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday', models.CharField(max_length=50)),
                ('monday', models.CharField(max_length=50)),
                ('tuesday', models.CharField(max_length=50)),
                ('wednesday', models.CharField(max_length=50)),
                ('thursday', models.CharField(max_length=50)),
                ('friday', models.CharField(max_length=50)),
                ('saturday', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
