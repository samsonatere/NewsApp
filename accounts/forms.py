from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from articles.models import Comment

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age', 'role')

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'role')

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']