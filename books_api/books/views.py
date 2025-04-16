from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer
 
# Create your views here.
 
class BookAPIListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
