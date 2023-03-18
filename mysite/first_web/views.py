from django.shortcuts import render
from django.http import HttpResponseRedirect
import os
import random

# Create your views here.

def index(request):
    return render(request, "first_web/index.html", {})

def get_random_image_path():
    path = os.path.join('static', 'images')
    images = os.listdir(path)
    image_path = os.path.join(path, random.choice(images))
    return image_path

def my_view(request):
    context = {'image_path': get_random_image_path()}
    return render(request, 'index.html', context)
