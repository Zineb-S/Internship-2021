from django.shortcuts import render
from .models import Question


def index(request):
    params = {"questions": Question.objects.all()}
    return render(request, "index.html", params)