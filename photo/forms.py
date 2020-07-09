from django import forms
from .models import Photo, Comment



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'text']
        # fields = '__all__'

        # widgets = {
        #     'photo':forms.ImageField(attrs={'class':'form-control'}),
        #     'text':forms.TextInput(attrs={'class': 'form-control'}),
        # }


class CommentForm(forms.ModelForm):
    '''
    댓글 모델 폼
    '''
    class Meta:
        model = Comment
        fields = ['comment_text']