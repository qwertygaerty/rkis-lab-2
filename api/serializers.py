from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Book, Author


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        baza = 'художественное произведение переведенное с другого языка'
        textbook = 'учебник'

        if Book.objects.filter(category=baza, publisher=data.get('publisher'),
                               author=data.get('author'),
                               title=data.get('title')).exists():
            raise serializers.ValidationError(
                'Такое художественное произведение переведенное с другого языка у этого издательства уже есть')

        if Book.objects.filter(category=textbook, publisher=data.get('yearOfRel'),
                               author__name=data.get('author'),
                               title=data.get('title')).exists():
            raise serializers.ValidationError('Такой учебник у этого издательства уже есть ')

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
