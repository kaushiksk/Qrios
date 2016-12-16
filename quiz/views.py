from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.

def home(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request, 'quiz/home.html',context=context)

    
