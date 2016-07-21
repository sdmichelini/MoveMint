from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
# Models
from project_feed.models import Organization, Project

from .forms import ProjectForm

def does_user_own(user, organization):
	return (user == organization.owner)

# Create your views here.

def index(request):
	orgs = get_list_or_404(Organization)
	return render(request, 'orgs/index.html', {'orgs' : orgs})

def detail(request, uuid):
	org = get_object_or_404(Organization, id=uuid)
	return render(request,'orgs/detail.html',{'org': org, 'is_owner': does_user_own(request.user, org)})

@permission_required('organization.can_add')
def create_project(request, uuid):
	org = get_object_or_404(Organization, id=uuid)
	if does_user_own(request.user, org):

		if request.method == 'POST':
			form = ProjectForm(request.POST)
			if form.is_valid():
				proj = Project(name = form.cleaned_data['name'],
 								about = form.cleaned_data['about'],
								org = org,
								donation_goal = form.cleaned_data['donation_goal'],
								start_date = form.cleaned_data['start_date'],
								end_date = form.cleaned_data['end_date'])
				proj.save()
				return redirect('/')
			else:
				return render(request, 'orgs/create_project.html', {'form': form})
		else:
			form = ProjectForm()
			return render(request, 'orgs/create_project.html', {'form': form})
	else:
		return redirect('index')

@permission_required('organization.can_add')
def create(request):
	if request.method == 'POST':
		if request.user.has_perm('organization.can_add'):
			if ('groupName' in request.POST) and ('about' in request.POST):
				try:
					org = Organization(name = request.POST['groupName'], about = request.POST['about'], owner=request.user)
					org.save()
					return redirect('index')
				except ValidationError, IntegrityError:
					return render(request, 'orgs/create.html', {'error':'Invalid request. Organization could not be processed.'}, status=400)
			else:
				return render(request, 'orgs/create.html', {'error':'Invalid request. Not enough data provided.'}, status=400)
			return render(request, 'orgs/create.html')
		else:
			return redirect('index')
	else:
		return render(request, 'orgs/create.html')
