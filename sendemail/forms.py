# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        })
    )
    subject = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'placeholder': "What's up?"
        })

    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's on your mind?"
        })
    )