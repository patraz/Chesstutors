from django import forms

from .models import Announcement, Avaliability, Comment




class AnnouncementForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'price', 'currency']
        labels = {
            'title': 'Tytuł',
            'content': 'Zawartość',
            'price': 'Cena za godzinę',
            'currency': 'Waluta'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": f'Announcement {str(field)}',
                "class": 'form-control',
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        self.fields['title'].widget.attrs.update({'rows': '2'})
        self.fields['content'].widget.attrs.update({'rows': '4'})

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Avaliability
        fields = ['day', 'av_from', 'av_to']
        labels = {
            'day': 'Dzień',
            'av_from': 'od',
            'av_to': 'do'
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        labels = {
            'content': 'Twój komentarz:',
            'rating': 'ocena'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'rows': '2'})
