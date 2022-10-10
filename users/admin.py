from django.contrib import admin
from .models import Profile
from .models import Illness, PhysicalActivities

admin.site.register(Profile)
admin.site.register(Illness)
admin.site.register(PhysicalActivities)
