from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
# Models
from project_feed.models import Organization


# Create your views here.

def index(request):
	orgs = get_list_or_404(Organization)
	return render(request, 'orgs/index.html', {'orgs' : orgs})

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
