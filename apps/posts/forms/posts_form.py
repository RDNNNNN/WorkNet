from django import forms
from django.forms.widgets import Select, Textarea, TextInput

from apps.posts.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "score",
        ]
        widgets = {
            "title": TextInput(attrs={"class": "mt-1 input-often-base"}),
            "content": Textarea(attrs={"class": "mt-1 textarea-often-base"}),
            "score": Select(attrs={"class": "mt-1 input-often-base"}),
        }
        labels = {
            "title": "標題",
            "content": "內文",
            "score": "評分",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"class": "w-full mt-1 textarea-often-base"}),
        }
        labels = {
            "content": "您想說些什麼",
        }

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop("post", None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        if self.post:
            comment.post = self.post
        if commit:
            comment.save()
        return comment