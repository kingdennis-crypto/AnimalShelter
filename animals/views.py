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