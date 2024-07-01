# blog/forms.py

from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'etiqueta', 'tag', 'image']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['image'].required = True  
            
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
