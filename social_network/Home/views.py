from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm,UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

def dashboard(request):
   
    return render(request,'Registration/dashboard.html',{'section': 'dashboard'})
    

def index(request):
    
    return render(request,'Registration/index.html')

def signup(request):
    if request.method=='GET':
        return render(request,'Registration/signup.html')
    elif request.method=='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
       
            new_user = user_form.save(commit=False)
        
            new_user.set_password(user_form.cleaned_data['password'])
        
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'Registration/register_done.html',{'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
            return render(request,'Registration/signup.html',{'user_form': user_form})


def logout_user(request):
    logout(request)
    return redirect(index)

def user_login(request):
    if request.method=='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            
            if user is not None:
                login(request, user)
                messages.success(request,"Successfully Logged In")
                return 
            
    else:
        form=LoginForm()
    return render(request, 'Registration/login.html', {'form':form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
        data=request.POST)
        profile_form = ProfileEditForm(
        instance=request.user.profile,
        data=request.POST,
        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
        instance=request.user.profile)
    return render(request,'Registration/edit.html',{'user_form': user_form,'profile_form': profile_form})
