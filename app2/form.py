from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *
class Form_login(forms.ModelForm):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password']
class UserCreationForms(UserCreationForm):
    username=forms.CharField(label='user name')
    password1=forms.CharField(label='password',min_length=8,widget=forms.PasswordInput())
    password2=forms.CharField(label='Password confirmation',min_length=8,widget=forms.PasswordInput())
    first_name=forms.CharField(label='first name')
    email=forms.CharField(label='email')
    last_name=forms.CharField(label='last name')
    
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email']



class Update_form(forms.ModelForm):
    first_name=forms.CharField(label='first name')
    email=forms.CharField(label='email')
    last_name=forms.CharField(label='last name')
    class Meta:
        model=User
        fields=('first_name','last_name','email')
        
class Update_profile(forms.ModelForm):

    class Meta:
        model=Profile
        fields=(
'name','subtitle','infor','adrees','adrees_detail','number_phone',
'working_hour','working_time','doctor_in','price','facebook','google','twitter',
'img','tybe')

class Comentform(forms.ModelForm):
    Name=forms.CharField(label='Name')
    email=forms.CharField(label='email')
    comment=forms.CharField(label='comment')
    img=forms.ImageField()
    class Meta:
        model=Comments
        fields=('Name','img','comment','email')

class Pastion(forms.ModelForm):
    class Meta:
        model=LOGIN
        fields=('name1','number','doctor','gender','data')


class Loginform(forms.ModelForm):
    
    class Meta:
        model=LOGIN
        fields='__all__'


class Blogform(forms.ModelForm):
    
    class Meta:
        model=Blogs
        fields='__all__'
class Comments_Form(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'
class ExpertDoctorForm(forms.ModelForm):
    class Meta:
        model=ExpertDoctor
        fields='__all__'
