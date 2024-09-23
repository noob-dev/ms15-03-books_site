# views.py
from struct import pack
from django.http import HttpResponse
from django.urls import reverse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    
    book_items = ''
    for book in books:
        book_items += f'<li><a href="{reverse("book_detail", args=[book.pk])}">{book.title}</a></li>'
    
    html = f"""
    <html>
    <head><title>Book List</title></head>
    <body>
        <h1>Books List</h1>
        <ul>
            {book_items}
        </ul>
    </body>
    </html>
    """
    
    return HttpResponse(html)


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

    html = f"""
    <html>
    <head><title>{book.title}</title></head>
    <body>
        <h1>{book.title}</h1>
        <p><strong>Author:</strong> {book.author}</p>
        <p>{book.description}</p>
        <a href="{reverse("book_list")}">Back to list</a>
    </body>
    </html>
    """
    
    return HttpResponse(html)
