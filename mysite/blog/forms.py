from django import forms
from django.core.validators import validate_email
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="Your Name",
        error_messages={
            "required": "Please enter your name.",
            "max_length": "Name should not exceed 50 characters.",
        },
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"}),
    )
    email = forms.EmailField(
        label="Your Email",
        validators=[validate_email],
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}),
    )
    to = forms.EmailField(
        label="Recipient's Email",
        widget=forms.EmailInput(attrs={"placeholder": "Enter recipient's email"}),
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Enter your comments"}),
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]


class SearchForm(forms.Form):
    query = forms.CharField()
