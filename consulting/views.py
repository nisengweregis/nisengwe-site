from django.shortcuts import render
from django.http import HttpResponse
from consulting.models import Consulting
# Create your views here.


def consulting_index(request):
    consultings = Consulting.objects.all()
    return render(request, 'consulting_index.html',
                  {'consultings': consultings})


def consulting_detail(request, pk):
    consulting = Consulting.objects.get(pk=pk)
    return render(request, 'consulting_detail.html',
                  {'consulting': consulting})