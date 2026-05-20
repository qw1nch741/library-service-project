from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 1. Define the main list of paths
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls', namespace='books')),
    path('api/borrowings/', include('borrowings.urls', namespace='borrowings')),
    path('api/users/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
