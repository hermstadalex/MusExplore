from django.db import models
from django.forms import ModelForm
from django.forms import extras
from django import forms

class Author(models.Model):
    dob = models.DateField(blank=True, null=True)

class AuthorForm(ModelForm):
    dob = forms.DateField(widget=extras.SelectDateWidget)
    class Meta:
        model = Author
        fields = ['dob']
