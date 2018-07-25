from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
  
class Thread(models.Model):
  name = models.CharField(max_length = 100)
  subject = models.CharField(max_length = 100)
  email = models.CharField(max_length = 80)
  body = models.TextField()
  timecreated = models.DateTimeField(auto_now_add = True) # how to set current time zone ??#} 
  active = models.BooleanField(default=True)    # used to deactivate inappropriate comments #}
  
  
  def __str__(self):
    return 'Comment by {} on {}'.format(self.name, self.subject)
  
class User(models.Model):
  name = models.CharField(max_length = 100, blank = True, null = True)
  password = models.CharField(max_length = 100, blank=True, null = True)
  mood = models.CharField(max_length = 100, blank = True, null = True)
  age = models.IntegerField();
    
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  
class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
