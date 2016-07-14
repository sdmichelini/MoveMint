from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def index(request):
	return render(request, 'me/me.html', {'user': request.user })

def login_view(request):
	if request.user.is_authenticated():
		return redirect('index')
	if request.method == 'POST':
		if ('username' in request.POST) and ('password' in request.POST):
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			print user
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
				else:
					return render(request, 'me/login.html', {'error':'Inactive User.'}, status = 403)
			else:
				return render(request, 'me/login.html', {'error':'Invalid Username and/or Password.'}, status = 403)
		else:
			return render(request, 'me/login.html', {'error':'Invalid Request. Username and password required'}, status = 400)
	else:
		return render(request, 'me/login.html', {})

def signup(request):
	return render(request, 'me/singup.html', {})

def logout_view(request):
	logout(request)
	return render(request, 'me/login.html', {})
