from django.shortcuts import render
from projects.models import Projects

def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', { 'projects': projects })

