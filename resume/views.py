from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from resume.models import Resume
# Create your views here.


def resume(request):
    return render(request, "work_experience.html")