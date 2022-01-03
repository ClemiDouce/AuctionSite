from django import forms
from comment.models import Comment


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['auction', 'content']
        
        