from django import forms
from .models import Item


class ItemForm(forms.ModelForm):               #creating a new class that inherits the ModelForm Class
    class Meta:                                 # innerclass 
        model = Item
        fields = ['name','done' ]                # defining fields that will pull into the form

