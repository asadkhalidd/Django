from django import forms
from .models import User
from django.forms import ModelForm, TextInput, TextInput

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["firstname", "lastname"]
        labels = {
            "firstname": "",
            "lastname": "",   
        }
        widgets = {
            'firstname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border: 0.5px solid #EFEFEF',
                'placeholder': 'First Name'
                
                }),
            'lastname': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px; border: 0.5px solid #EFEFEF; margin-top: 5%;',
                'placeholder': 'Last Name',
                
                })
        }


    
   
   
    
    
    
    
        