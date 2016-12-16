from django.db import models
from django.contrib.auth.models import User
from quiz.models import Question
from django.db.models.signals import post_save
# Create your models here.

class Quizzer(models.Model):
    user        = models.OneToOneField(User)
    name        = models.CharField(max_length=200)
    answered    = models.ManyToManyField(Question,blank=True)
    points      = models.IntegerField(default=0)

    def __str__(self):
        return self.name

#def create_quizzer_user_callback(sender,instance,**kwargs):
#    quizzer,new = Quizzer.objects.get_or_create(user=instance)

#post_save.connect(create_quizzer_user_callback,User)
