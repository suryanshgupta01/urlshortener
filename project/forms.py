from .models import shortURL
from django import forms

class createnewshorturl(forms.ModelForm):
    class Meta:
        model = shortURL
        fields = ['og_url']
        widgets = {
            'short_url': forms.TextInput(attrs={'class':'form-control'}),
            'og_url': forms.TextInput(attrs={'class':'form-control'}),
        }