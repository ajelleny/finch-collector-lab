from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Dog, Toy
from .forms import FeedingForm

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

@login_required
def dogs_index(request):
  # retrives all dogs from db
  dogs = Dog.objects.filter(user=request.user)
  return render(request, 'dogs/index.html', { 'dogs': dogs })

@login_required
def dogs_new(request):
  # create new instance of dog form filled with submitted values or nothing
  dog_form = DogForm(request.POST or None)
  # if the form was posted and valid
  if request.POST and dog_form.is_valid():
    new_dog = dog_form.save(commit=False)
    new_dog.user = request.user
    new_dog.save()
    # redirect to index
    return redirect('index')
  else:
    # render the page with the new dog form
    return render(request, 'dogs/new.html', { 'dog_form': dog_form }) 

@login_required
def dogs_detail(request, dog_id):
  # retrieve a single dog using an id
  dog = Dog.objects.get(id=dog_id)
  # get toys the dog doesnt have
  toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
  # create an instance of the feeding form 
  feeding_form = FeedingForm()
  context = {
    'dog': dog,
    'feeding_form': feeding_form,
    'toys': toys_dog_doesnt_have
  }
  return render(request, 'dogs/detail.html', context)

@login_required
def add_feeding(request, dog_id):
  # create the model form using dating stored in the post request 
  form = FeedingForm(request.POST)
  # validate the form 
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)

@login_required
def assoc_toy(request, dog_id, toy_id):
  dog = Dog.objects.get(id=dog_id)
  dog.toys.add(toy_id)
  return redirect('detail', dog_id=dog_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      print(form.errors.as_json())
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

