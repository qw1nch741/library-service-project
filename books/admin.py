from django.contrib import admin
from .models import Book

# Standard registration
admin.site.register(Book)

# OR: Use a custom ModelAdmin to display specific columns in the admin panel
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date') # Adjust fields to match your model
    search_fields = ('title', 'author')