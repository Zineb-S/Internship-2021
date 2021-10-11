from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import os
import subprocess

from django.urls import reverse
import random

import folders
from random import choice
from django.http import HttpResponseRedirect
from .forms import PathForm
from .models import PathFolder


def index(request):
    global context
    if request.method == 'POST' and 'run_script' in request.POST:
        # import function to run
        import scripti
        # call function
        x = scripti.Folder('hi')
        val = x.printing()
        context = {'number': val}
        nums = [1, 2, 3, 4, 5]
        # context = {"number": choice(nums)}
        # return user to required page
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PathForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PathForm()

    return render(request, "index.html")  # ,context


def path_create_view(request):
    form = PathForm(request.POST or None)
    if form.is_valid():
        form.save()


def result(request):
    inp_value = request.POST.get('your_name', 'This is a default value')
    context = {'inp_value': inp_value}
    return render(request, "result.html", context)