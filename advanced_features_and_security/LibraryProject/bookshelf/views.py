from __future__ import annotations
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm, ExampleForm
from .models import Book


def example_form_view(request):
	"""
	Simple view demonstrating usage of ExampleForm with CSRF protection.
	"""
	if request.method == "POST":
		form = ExampleForm(request.POST)
		if form.is_valid():
			return redirect("/")
	else:
		form = ExampleForm()
	return render(request, "bookshelf/form_example.html", {"form": form})


@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
	books = Book.objects.select_related("created_by").all()
	return render(request, "bookshelf/book_list.html", {"books": books})


@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			book.created_by = request.user
			book.save()
			return redirect("book_list")
	else:
		form = BookForm()
	return render(request, "bookshelf/form_example.html", {"form": form, "action": "Create"})


@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id: int):
	book = get_object_or_404(Book, id=book_id)
	if request.method == "POST":
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect("book_list")
	else:
		form = BookForm(instance=book)
	return render(request, "bookshelf/form_example.html", {"form": form, "action": "Edit"})


@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id: int):
	book = get_object_or_404(Book, id=book_id)
	if request.method == "POST":
		book.delete()
		return redirect("book_list")
	return render(request, "bookshelf/confirm_delete.html", {"book": book})


