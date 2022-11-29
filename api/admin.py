from django.contrib import admin

# Register your models here.


from django.contrib import admin
from api.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
