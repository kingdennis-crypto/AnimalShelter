from django.urls import path
from .views import *

urlpatterns = [
  path('', homePage, name="HomePage"),
  path('about/', aboutPage, name="AboutPage"),
  path('animals/', animalsPage, name="AnimalsPage"),
  path('animal/<str:id>', animalProfile, name="AnimalProfile"),
]