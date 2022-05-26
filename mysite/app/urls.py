from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generation/', views.generation, name='generation'),
    path('model/', views.model, name='model'),
    path('brand/', views.brand, name='brand'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('formBrand/', views.formBrand, name='formBrand'),
]