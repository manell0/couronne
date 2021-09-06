from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django.utils.translation import gettext_lazy as _
from django.core import validators

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Lösenord', help_text='<h5>Håll reda på ditt löseord!</h5>')
    class Meta():
        model = User
        fields = ('username','password','email')

        labels = {"username":"Användarnamn","email":"Email"}
        help_texts = {'username': _(''),'email': _('<h5> Email krävs för att deltaga i couronne.se tävlingar och evenemang! T.ex SM i couronne.</h5>')}
        


        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():   
        model = UserProfileInfo
        fields = ['club_location']

        labels = {"club_location":"Klubb"}
        help_texts = {'club_location': _('<h5>Klubb / Spelställe (hemma eller skolan, jobbet) / Ort</h5>')}
        error_messages = {'club_location': {'max_length': _("Nämen så där långt... Max 40 tecken!")}}


class UppForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Lösenord', help_text='<h5>Skriv in ditt löseord här... (eller om du vill byta lösenord så skriver du in det)!</h5>')
    class Meta():
        model = User
        fields = ('password', 'email')

        labels = {"username":"Användarnamn","email":"Email","first_name":"Ditt namn"}
        help_texts = {'username': _(''),'email': _('<h5>Giltig emailadress krävs för giltiga ratingpoäng, samt att få delta i tävlingar och evenemang! T.ex couronne SM.</h5>')}
        error_messages = {'username': {'max_length': _("Nämen så där långt... Max 40 tecken!")}}

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
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)