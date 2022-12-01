from rest_framework import serializers
from rest_framework import viewsets, filters, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Book, Author
from api.serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "genre", "author__name"]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        item = BookSerializer(data=request.data)
        print(Book.objects.filter(author=request.data.get('author'))[0].author)
        print(request.data.get('title'))
        print(request.data.get('author'))
        print(request.data.get('yearOfRel'))
        print(request.data.get('genre'))
        print(request.data.get('category'))
        print(request.data.get('publisher'))
        print(request.data.get('photoPreview'))
        print(request.data.get('bookFile'))

        if item.is_valid():
            item.save()
            return Response('Книга успешно добавлена ура ура')
        else:
            return Response('Книга неуспешно недобавлена неура неура', status=status.HTTP_400_BAD_REQUEST)
