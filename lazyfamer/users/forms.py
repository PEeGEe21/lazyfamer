from pyexpat import model
from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email', 'first_name', 'last_name', 'password')

    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserUpdateForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
