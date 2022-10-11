from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from embed_video.fields import EmbedVideoField


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    User._meta.get_field('email')._unique = True
    def __str__(self):
        return self.user.username
    
class Illness(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    added = models.DateTimeField(auto_now_add=True)
    symptoms = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    treatment = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class PhysicalActivities(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-added']

class DietSupplement(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, choices=(('vitamins', 'VITAMINS'),('food', 'FOOD'),), default = 'vitamins')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    classification = models.CharField(max_length=50, choices=(
    ('underweight','UNDERWEIGHT'),
    ('overweight', 'OVERWEIGHT'),
    ('obese','OBESE'),
    ('normal','NORMAL'),), default='normal')

    def __str__(self):
        return self.category + ": "+self.name

class DietPlan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    breakfast = models.CharField(max_length=150)
    snacks = models.CharField(max_length=150)
    lunch = models.CharField(max_length=150)
    dinner = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    


    