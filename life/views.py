from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from life.models import *
from life.forms import ThreadForm
from life.forms import UserForm
from life.forms import LoginForm


def index(request):
 # all_groups= Group.objects.all()
  #return render(request, 'life/index.html',{
  #    "groups": all_groups,
 # })
  form= ThreadForm(request.POST or None)
  if form.is_valid():
    form.save()
  
  context= {'form': form }
        
  return render(request, 'life/index.html', context)
  
  
def group(request):
 
  return render(request, "life/group.html")


def usercreation(request):
  form= UserForm(request.POST or None)
  if form.is_valid():
    form.save()
  
  context= {'form': form }
  return render(request, "life/usercreation.html", context)



def profile(request):
    profiles = User.objects.all()
    return render(request, 'life/profile.html', {'profiles': profiles,})
  
def userview(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    name = {"form": form}
    return render(request, 'life/userview.html', name)
  
def viewthread(request):
    threads = Thread.objects.all()
    return render(request, 'life/viewthread.html', {"threads": threads,})




def showform(request):
    form= ThreadForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'life/index.html', context)

  
