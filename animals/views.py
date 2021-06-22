from django.shortcuts import render

def homePage(request):
  return render(request, 'animals/home.html')

def aboutPage(request):
  return render(request, 'animals/about.html')

def animalsPage(request):
  return render(request, 'animals/animals.html')