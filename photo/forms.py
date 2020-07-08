from django import forms
from .models import Photo



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'text']
        # fields = '__all__'

        # widgets = {
        #     'photo':forms.ImageField(attrs={'class':'form-control'}),
        #     'text':forms.TextInput(attrs={'class': 'form-control'}),
        # }