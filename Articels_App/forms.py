from django import forms
from Articels_App.models import Sys_user , Comment , Article
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username' , 'password' , 'email')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
