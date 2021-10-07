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
        fields = ('username', 'password', 'email')
        labels = {"username": "UserName"}
        help_texts = {'username': _(''), 'email': _('')}

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


# Main form for registration of players
class UserProfileInfoForm(forms.ModelForm):
    class Meta():

        model = UserProfileInfo
        fields = ['club_location']
        labels = {"club_location": "The Club"}
        help_texts = {'club_location': _('<br> Join or create your club.')}
        error_messages = {'club_location': {'max_length': _("Too long ... Max 40 characters!")}}


# Modelform for the player update
class UppForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', help_text='<br>Enter your new password (or the old password)')

    class Meta():

        model = User
        fields = ('password', 'email')
        labels = {"username": "User Name", "email": "EmailAdd", "first_name": "Your Name"}
        help_texts = {'username': _(''), 'email': _('<br>A valid email is required for valid rating points!')}
        error_messages = {'username': {'max_length': _("Too long ... Max 40 characters!")}}


# Form for logged in user when register match
class UserMatchForm(forms.ModelForm):
    class Meta():

        model = User
        fields = ['username']
        labels = {"username": ""}
        help_texts = {'username': _('')}


# Form for oponent when register match
class UserMatchFormOpponent(forms.ModelForm):
    class Meta():

        model = User
        fields = ['first_name']


# Form for use when user contact us
class ContactForm(forms.Form):

    from_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass myfieldclass-small myfieldclass-medium', 'placeholder': 'Email'}), label='')
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass myfieldclass-small myfieldclass-medium', 'placeholder': 'Subject'}), label='')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'myfieldclass myfieldclass-small myfieldclass-medium', 'placeholder': 'Message'}), label='')
