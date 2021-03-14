from django.shortcuts import render, redirect
from .models import Dog
from .forms import FeedingForm

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
  # retrieve a single dog using an id
  dog = Dog.objects.get(id=dog_id)
  # create an instance of the feeding form 
  feeding_form = FeedingForm()
  context = {
    'dog': dog,
    'feeding_form': feeding_form
  }
  return render(request, 'dogs/detail.html', context)

def add_feeding(request, dog_id):
  # create the model form using dating stored in the post request 
  form = FeedingForm(request.POST)
  # validate the form 
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)