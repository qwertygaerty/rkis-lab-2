from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
