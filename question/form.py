from django import forms
from  django.contrib.auth.models import User
from myapp.models import UserProfile


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dob', 'bio','city','image']




