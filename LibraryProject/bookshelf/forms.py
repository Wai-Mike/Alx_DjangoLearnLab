from django import forms
from .models import Book


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_on"]


