from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import AnswerForm
from quizzer.models import Quizzer

# Create your views here.

def home(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request, 'quiz/home.html',context=context)

def detail(request,questionid):
    question = get_object_or_404(Question,pk=questionid)
    if request.user.is_anonymous():
        return HttpResponseRedirect('/login/')
    form = AnswerForm()
    context = {'question':question,
                'form':form}
    return render(request, 'quiz/details.html',context=context)

def answer(request,questionid):
    question = get_object_or_404(Question,pk=questionid)
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.cleaned_data['answer']
        if answer != question.answer:
            return render(request, 'quiz/details.html', {
                'question': question,
                'form':form,
                'error_msg': "Sorry, Wrong Answer",
            })
        else:
            quizzer = request.user.quizzer
            quizzer.answered.add(question)
            quizzer.points += question.points
            request.user.save()
            return HttpResponseRedirect(reverse('quiz:home'))
    else:
        return render(request, 'quiz/details.html', {
            'question': question,
            'form':form,
        })

def leaderboard(request):
    quizzers = Quizzer.objects.all().order_by('-points')
    context = {'quizzers': quizzers}
    return render(request, 'quiz/leaderboard.html',context=context)
