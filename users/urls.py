from django.urls import path
from .views import index, profile, RegisterView, children
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('childlist/', children, name='childlist' ),
    path('childlist/<int:id>', views.view_child, name='view_child'),
    path('childlist/add/', views.add_child, name='child_add'),
    path('childlist/edit/<int:id>', views.edit_child, name='child_edit'),
    path('childlist/delete/<int:id>', views.delete_child, name='deletechild'),
]
