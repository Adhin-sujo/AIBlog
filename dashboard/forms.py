from django import forms
from .models import BlogPost

class BlogGenerateForm(forms.Form):
    title = forms.CharField(max_length=255)
    tone = forms.CharField(max_length=255)
    style = forms.CharField(max_length=255)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content')