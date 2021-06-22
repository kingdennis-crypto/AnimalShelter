from django.shortcuts import render
from .models import animal

def homePage(request):
  return render(request, 'animals/home.html')

def aboutPage(request):
  return render(request, 'animals/about.html')

def animalsPage(request):
  animals = animal.objects.all()

  context = {'animals':animals}
  return render(request, 'animals/animals.html', context)

def animalProfile(request, id):
  object = animal.objects.get(id=id)
  
  context = {'animal':object}
  return render(request, 'animals/animalProfile.html', context)