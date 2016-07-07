from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Project

def index(request):
	projects = get_list_or_404(Project)
	return render(request,'project_feed/index.html',{'projects': projects})

def detail(request, uuid):
	project = get_object_or_404(Project, id=uuid)
	return render(request,'project_feed/detail.html',{'project': project})
