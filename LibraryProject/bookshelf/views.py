from django.shortcuts import render, redirect
from .forms import ExampleForm


def example_form_view(request):
    """
    Simple view demonstrating usage of ExampleForm.
    """
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Normally process the data, then redirect.
            return redirect("/")
    else:
        form = ExampleForm()
    return render(request, "form_example.html", {"form": form})


