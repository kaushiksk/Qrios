from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    answer = models.CharField(max_length=200)
    points = models.IntegerField(default=10)
    def __str__(self):
        return self.name
