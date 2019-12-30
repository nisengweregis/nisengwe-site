from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailField(
        required = True,
        max_length=60,
        widget=forms.TextInput(attrs={"class": "form-control",
            "placeholder": "Your Email"})
    )
    first_name = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'placeholder': "first name"
        }))
    last_name = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            'placeholder': "last name"
        }))

    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "What's on your mind?"
        }))


    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')


#class ContactForm(forms.Form):
