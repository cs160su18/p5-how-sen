from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from life.models import *
from life.forms import ThreadForm


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
  return render(request, "life/usercreation.html")












def showform(request):
    form= ThreadForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'life/index.html', context)

  
