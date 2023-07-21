from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Author, Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"

    