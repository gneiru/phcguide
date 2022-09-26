from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class Child(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    child_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=[(MALE,'Male'),(FEMALE,'Female')], default=MALE)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    street = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Child: {self.first_name} {self.last_name} \n Parent: {self.parent_name}'

