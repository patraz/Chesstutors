from django import forms

from .models import Userprofile


class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['description']
        labels = {
            'description': 'Zmień opis'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '1'})

class UserprofilePhoto(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['profile_picture']
        labels = {
            'profile_picture': 'zdjęcie profilowe'
        }
    
