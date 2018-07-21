from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from life.models import *

def index(request):
  all_group= Group.object.all()
  return render(request, 'life/index.html',{"group":all_group})
