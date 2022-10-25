from django.contrib import admin
from .models import Illness, PhysicalActivities, DietPlan, DietSupplement, DietSchedule

admin.site.register(DietPlan)
admin.site.register(DietSupplement)
admin.site.register(PhysicalActivities)
admin.site.register(Illness)
admin.site.register(DietSchedule)
