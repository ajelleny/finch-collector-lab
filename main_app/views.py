from django.shortcuts import render
from .models import Dog

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  # retrives all dogs from db
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
  # retrieve a single cat using an id
  dog = Dog.objects.get(id=dog_id)
  return render(request, 'dogs/detail.html', { 'dog': dog })