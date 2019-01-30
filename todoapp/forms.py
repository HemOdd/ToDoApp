from django import forms
from .models import fileModel

class fileForm(forms.ModelForm):
    class Meta:
        model = fileModel
        fields = ('mediaFile',)