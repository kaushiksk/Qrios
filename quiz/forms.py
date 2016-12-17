from django import forms
from django.forms import ModelForm

class AnswerForm(forms.Form):
    answer        = forms.CharField(label=(u'Answer'))
