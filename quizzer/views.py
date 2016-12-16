from django.shortcuts import render
from django.http import HttpResponseRedirect
from quizzer.forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User
from .models import Quizzer
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def QuizzerRegistration(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/home/')
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        user = User.objects.create_user(username=form.cleaned_data['username'],
                                                        email = form.cleaned_data['email'], password = form.cleaned_data['password'])
                        user.save()
                        quizzer = Quizzer(user=user, name=form.cleaned_data['name'])
                        quizzer.save()
                        return HttpResponseRedirect('/home/')
                else:
                        return render(request,'quizzer/register.html', context = {'form': form})

        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form}
                return render(request,'quizzer/register.html', context=context)

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            quizzer = authenticate(username=username, password=password)
            if quizzer is not None :
                login(request,quizzer)
                return HttpResponseRedirect('/home/')
            else:
                return render(request,'quizzer/login.html', context = {'form': form})
        else:
            return render(request,'quizzer/login.html', context = {'form': form})


    else:
        ''' user is not submitting the form, show them a blank registration form '''
        form = LoginForm()
        context = {'form':form}
        return render(request, 'quizzer/login.html', context = context)


def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/login/')
