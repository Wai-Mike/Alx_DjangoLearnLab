from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_on"]


class ExampleForm(forms.Form):
    """
    Simple example form to demonstrate CSRF usage and safe input handling.
    """
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")

