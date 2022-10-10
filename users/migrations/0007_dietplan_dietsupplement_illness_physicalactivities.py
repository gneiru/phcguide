# Generated by Django 4.1.1 on 2022-10-10 10:07

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_profile_avatar_remove_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('breakfast', models.CharField(max_length=150)),
                ('snacks', models.CharField(max_length=150)),
                ('lunch', models.CharField(max_length=150)),
                ('dinner', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='DietSupplement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('vitamins', 'VITAMINS'), ('food', 'FOOD')], default='vitamins', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('classification', models.CharField(choices=[('underweight', 'UNDERWEIGHT'), ('overweight', 'OVERWEIGHT'), ('obese', 'OBESE'), ('normal', 'NORMAL')], default='normal', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('symptoms', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('treatment', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=None)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PhysicalActivities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
