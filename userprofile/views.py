
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserprofileForm, UserprofilePhoto, UserPhoneNumber
from announcements.models import Announcement
# Create your views here.

from .models import Userprofile

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = Userprofile.objects.create(user=user)

            login(request, user)

            return redirect("/")
        
    else:
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return render(request, 'login/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

def edit_description_hx(request):
    user = get_object_or_404(Userprofile, user=request.user)
    form = UserprofileForm(request.POST or None, instance = user)
    context = {
        "form":form,
        'user': user
    }
    if request.POST:
        if form.is_valid():
            form.save()
        return render(request, 'about_me.html', context)
    return render(request, 'description_edit_form.html', context)


def edit_number_hx(request):
    user = get_object_or_404(Userprofile, user=request.user)
    form = UserPhoneNumber(instance = user)
    context = {
        'form':form,
        'user': user
    }
    if request.method == 'POST':
        form = UserPhoneNumber(request.POST or None, instance = user)
        print('yo')
        if form.is_valid():
            print('yo')
            form.save()
        return render(request, 'phone_number.html', context)
    return render(request, 'phone_edit.html', context)

def upload_photo(request):
    user = get_object_or_404(Userprofile, user= request.user)
    form = UserprofilePhoto(request.POST or None)
    
    context = {
        'form': form,
        'user':user
    }

    if request.method == 'POST':
        form = UserprofilePhoto(request.POST or None, request.FILES, instance = user)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request, 'upload_photo.html', context)

def show_number(request, id=None):
    author = get_object_or_404(Userprofile, id = id)
    context = {
        'author': author
    }
    return render(request, 'number.html', context)
