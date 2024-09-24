from django import forms
from .models import Submission


class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Submission.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already registered.")
        return email
