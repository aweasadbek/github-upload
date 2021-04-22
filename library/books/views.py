from django.views.generic import ListView
from .models import Book

# Create your views here.

class HomePage(ListView):
    template_name = "home.html"
    model = Book
    context_object_name = "book_list"
