from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_view(request):
  if request.user.is_authenticated:
    messages.info(request, f'You are already logged in as {request.user.username}.')
    return redirect('main:home')

  if request.method == 'POST':
    login_form = AuthenticationForm(request=request, data=request.POST)
    if login_form.is_valid():
      username = login_form.cleaned_data.get('username')
      password = login_form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        # there is user
        login(request, user)
        messages.success(request, f'You are now logged in as { username }.')
        return redirect('main:home')
      else:
        messages.error(request, f'An error occurred trying to login.')
    
    else:
      messages.error(request, f'An error occurred trying to login.')
  elif request.method == 'GET':
    login_form = AuthenticationForm()

  return render(request, 'accounts/login.html', {"login_form": login_form})


@login_required
def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('main:home')
  else:
    return render(request, 'accounts/logout.html', {})