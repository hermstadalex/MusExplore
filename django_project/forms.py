from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ArtistForm(forms.Form):
    artist_name = forms.CharField(label='', max_length=100,
            widget=forms.TextInput(attrs={'class': "form-control"}))
