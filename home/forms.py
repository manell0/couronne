from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django.utils.translation import gettext_lazy as _
from django.core import validators

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password ')
    email = forms.EmailField(required=True, label='EmailAdd ')
    class Meta():
        model = User
        fields = ('username','password','email')
        labels = {"username":"UserName"}
        help_texts = {'username': _(''),'email': _('')}

        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():   
        model = UserProfileInfo
        fields = ['club_location']
        labels = {"club_location":"Club/Loc"}
        help_texts = {'club_location': _('<br>Club / Venue (home or school, work) / Location')}
        error_messages = {'club_location': {'max_length': _("Too long ... Max 40 characters!")}}


class UppForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', help_text='<br>Enter your new password (or the old password)')
    class Meta():
        model = User
        fields = ('password', 'email')
        labels = {"username":"User Name","email":"EmailAdd","first_name":"Your Name"}
        help_texts = {'username': _(''),'email': _('<br>A valid email is required for valid rating points!')}
        error_messages = {'username': {'max_length': _("Too long ... Max 40 characters!")}}

class UserMatchForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username']
        labels = {"username":""}
        help_texts = {'username': _('')}

        
class UserMatchFormOpponent(forms.ModelForm):
    class Meta():
        model = User
        fields = ['first_name']


class ContactForm(forms.Form):
    
    from_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass myfieldclass-small myfieldclass-medium', 'placeholder': 'Email'}), label='')  
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass myfieldclass-small myfieldclass-medium', 'placeholder': 'Subject'}), label='')  
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'myfieldclass myfieldclass-small myfieldclass-medium', 'placeholder': 'Message'}), label='')  
    
