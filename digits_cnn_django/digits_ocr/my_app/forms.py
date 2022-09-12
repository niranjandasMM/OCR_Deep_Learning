from django import forms
 
from django.forms import fields  
from django import forms  
  
  
from django import forms 
  
class ImagefieldForm(forms.Form): 
    name = forms.CharField() 
    image_field = forms.ImageField() 