from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserInfo(User):
    contact=models.CharField(max_length=30)
    age=models.IntegerField(null=True)
    address=models.TextField(max_length=500,null=True)

    class Meta:
        db_table='userinfo'


class UserInfoForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','email','age','contact','address','password1','password2']
        
        
class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','password1','password2']
