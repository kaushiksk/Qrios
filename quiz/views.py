from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request, 'quiz/home.html',context=context)
