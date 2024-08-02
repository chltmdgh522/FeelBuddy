from django import forms
from .models import Community, Comment

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title', 'content', 'img_url']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
