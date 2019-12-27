from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project
# Create your views here.


def project_index(request):
    projects = Project.objects.all()
    return render(request, 'project_index.html',
                  {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html',
                  {'project': project})