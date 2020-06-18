from django import forms
from .models import List
from django.contrib.auth.models import User


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]

    
