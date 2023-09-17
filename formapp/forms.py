from django import forms
from .models import User


class UserSignUp(forms.ModelForm):
    verify_email = forms.EmailField(label="Verify Email")

    class Meta:
        model = User
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        verify_email = cleaned_data.get("verify_email")

        if email != verify_email:
            raise forms.ValidationError("Email addresses do not match.")

        return cleaned_data
