from django.db import models
from django.contrib.auth.models import User

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    User._meta.get_field('email')._unique = True
    def __str__(self):
        return self.user.username
    
class Illness(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    added = models.DateTimeField(auto_now_add=True)
    symptoms = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    treatment = models.CharField(max_length=50, blank=True)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class PhysicalActivities(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=50)
    classification = models.CharField(max_length=50, choices=(
    ('underweight','UNDERWEIGHT'),
    ('overweight', 'OVERWEIGHT'),
    ('obese','OBESE'),
    ('normal','NORMAL'),), default='normal')
    
    def __str__(self):
        return f"{self.classification}: {self.title}"
    class Meta:
        ordering = ['-added']

class DietSupplement(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, choices=(('vitamins', 'VITAMINS'),('food', 'FOOD'),), default = 'vitamins')
    name = models.CharField(max_length=50,unique=True)
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
    name = models.CharField(max_length=50,unique=True)
    breakfast = models.CharField(max_length=150)
    snacks = models.CharField(max_length=150)
    lunch = models.CharField(max_length=150)
    dinner = models.CharField(max_length=150)
    classification = models.CharField(max_length=50, choices=(
    ('underweight','UNDERWEIGHT'),
    ('overweight', 'OVERWEIGHT'),
    ('obese','OBESE'),
    ('normal','NORMAL'),), default='normal')


    def __str__(self):
        return self.name

class DietSchedule(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sunday = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True, related_name='sunday')
    monday = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True, related_name='monday')
    tuesday = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True, related_name='tuesday')
    wednesday = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True, related_name='wednesday')
    thursday = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True, related_name='thursday')
    friday = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True, related_name='friday')
    saturday = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True, related_name='saturday')

    def __str__(self):
        return f"DietSched of {self.user}"  
    
    


    