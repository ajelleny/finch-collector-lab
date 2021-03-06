from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('about/', views.about, name="about"),
    path('dogs/', views.dogs_index, name="index"),
    path('dogs/new', views.dogs_new, name="new"),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name="add_feeding"),
    path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy"),
    path('accounts/signup/', views.signup, name='signup'),
]