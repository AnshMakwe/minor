from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('projects')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'projects')
        else:
            messages.error(request, 'username or password is incorrect!')

    context = {
        'page': page,
    }
    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'user loged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'user account was created!')
            login(request, user)
            return redirect('edit-account')
        else:
            messages.success(request, 'an error has occurred during registration!')
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            return redirect('account')
    context = {
        'form': form,
    }
    return render(request, 'users/profile_form.html', context)










