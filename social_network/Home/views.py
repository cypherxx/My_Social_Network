from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def dashboard(request):
   
    return render(request,'Registration/dashboard.html',{'section': 'dashboard'})
    

def index(request):
    
    return render(request,'Registration/index.html')

def signup(request):
    if request.method=='GET':
        return render(request,'Registration/signup.html')
    else:
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
       
            new_user = user_form.save(commit=False)
        
            new_user.set_password(
            user_form.cleaned_data['password'])
        
            new_user.save()
        return render(request,'account/register_done.html',{'new_user': new_user})

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
