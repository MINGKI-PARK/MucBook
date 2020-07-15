from django import forms
from .models import TastyComment



class TastyCommentForm(forms.ModelForm):
    '''
    댓글 모델 폼
    '''
    class Meta:
        model = TastyComment
        fields = ['comment_text', 'score']