from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Projects


def index(request):
    projects = Projects.objects.all()
    return render(request, 'projects/index.html', { 'projects': projects })

def detail(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    return render(request, 'projects/detail.html', { 'project': project })
    