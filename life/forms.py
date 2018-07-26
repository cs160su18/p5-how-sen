from django import forms
from .models import Thread
from .models import User
from .models import Login

class ThreadForm(forms.ModelForm):
    class Meta:
        model= Thread
        fields= ["name", "subject", "email", "body"]
        
        
        
class UserForm(forms.ModelForm):
  class Meta:
      model = User
      fields = ["name", "mood", "age"]
      
      
class LoginForm(forms.ModelForm):
  class Meta:
      model = Login
      fields = ["name"]
      
        
        

        