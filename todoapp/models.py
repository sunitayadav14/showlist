from django.db import models

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class List(models.Model):
    Number=models.IntegerField()
    Title=models.CharField(max_length=50)
    Date=models.DateField()
    description=models.TextField(max_length=400)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="list"


class ListForm(forms.ModelForm):
    class Meta:
        model=List
        fields='__all__'
