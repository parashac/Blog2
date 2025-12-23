from django import forms
from blog_app.models import POST

class PostForm(forms.ModelForm):
    class Meta:
        model = POST
        fields =['title', 'content']