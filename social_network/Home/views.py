from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def index(request):
    return render(request,'Registration/index.html')

# def user_login(request):
#     if request.method=='POST':
#         form= LoginForm(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 login(request, user)
#                 return HttpResponse('Authenticated successfully')
#             else:
#                 return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid login')
#     else:
#         form=LoginForm()
#     return render(request, 'Home/login.html', {'form':form})
