from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters, status
from rest_framework import permissions
from rest_framework import serializers
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


@api_view(['POST'])
def add_book(request):
    item = BookSerializer(data=request.data)
    print(request.data.get('publisher'))
    baza = 'художественное произведение переведенное с другого языка'
    textbook = 'учебник'

    if Book.objects.filter(category=baza, publisher=request.data.get('publisher'),
                           title=request.data.get('title')).exists():
        raise serializers.ValidationError(
            'Такое художественное произведение переведенное с другого языка у этого издательства уже есть')

    if Book.objects.filter(category=textbook, publisher=request.data.get('yearOfRel'),
                           author__name=request.data.get('author'),
                           title=request.data.get('title')).exists():
        raise serializers.ValidationError('Такой учебник у этого издательства уже есть ')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
