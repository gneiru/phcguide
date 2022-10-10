from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='users-register'),
    path('profile/', views.profile, name='users-profile'),
    path('bmi/', views.bmi, name='bmi'),
    path('diet/plan/', views.diet_plan, name='diet_plan'),
    path('diet/supplement/', views.diet_supplement, name='diet_supplement'),
    path('activities/', views.activities, name='activities'),
    path('common_illness/', views.common_illness, name='common_illness'),
]
