from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import permission_required
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
			print(request.POST)
			return render(request, 'orgs/create.html')
		else:
			return redirect('index')
	else:
		return render(request, 'orgs/create.html')
