from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ArtistForm(forms.Form):
    """
        Form for artist name on front page.
    """
    artist_name = forms.CharField(label='', max_length=100,
            widget=forms.TextInput(attrs={'class': "form-control"}))

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)


    reason = forms.ChoiceField(choices=[('Feedback', 'Feedback'), ('Help', 'Help'), ('Jobs', 'Jobs'), ('Report a bug','Report a bug'), ('Other', 'Other')])


    content = forms.CharField(
            required=True,
            widget=forms.Textarea
    )



    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
        self.fields['reason'].label = "Reason for Contacting"
        
