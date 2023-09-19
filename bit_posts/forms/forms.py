from django import forms
from bit_posts.models.post import Comment,SubComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ReplyToCommentForm(forms.ModelForm):
    class Meta:
        model = SubComment  #Child model for Comment Model
        fields = ['text']
