from django import forms
from blog.models import Post , Category
from tinymce.widgets import TinyMCE


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =[
            'title',
            'cover_image',
            'content',
            'category',
        ]

    