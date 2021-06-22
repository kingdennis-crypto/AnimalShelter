from django.shortcuts import render

def homePage(request):
  return render(request, 'animals/home.html')

def aboutPage(request):
  return render(request, 'animals/about.html')