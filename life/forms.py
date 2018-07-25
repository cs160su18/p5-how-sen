from django import forms
from .models import Thread
from .models import User

class ThreadForm(forms.ModelForm):
    class Meta:
        model= Thread
        fields= ["name", "subject", "email", "body"]
        
        
        
class UserForm(forms.ModelForm):
  class Meta:
      model = User
      fields = ["name", "password", "mood"]
        
        
        