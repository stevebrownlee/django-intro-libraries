from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "libraryapp"
urlpatterns = [
    url(r'^books$', list_books, name='list_books'),
    url(r'^librarians$', list_librarians, name='list_librarians'),
    url(r'accounts/', include('django.contrib.auth.urls')),
]
