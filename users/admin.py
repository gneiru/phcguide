from django.contrib import admin
from .models import Illness, PhysicalActivities, DietPlan, DietSupplement

admin.site.register(DietPlan)
admin.site.register(DietSupplement)
admin.site.register(PhysicalActivities)
admin.site.register(Illness)
