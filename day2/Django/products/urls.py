from django.urls import path
from django.views.generic.list import ListView

from .views import BookDetailView, BookListView

urlpatterns = [
    path("books", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>", BookDetailView.as_view(), name="book-detail")
]