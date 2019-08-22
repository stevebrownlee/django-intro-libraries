from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "libraryapp"
urlpatterns = [
    url(r'^books$', list_books, name='list_books'),
    url(r'^books/(?P<book_id>[0-9]+)/$', book_details, name="book_details"),
    url(r'^book$', create_book, name='create_book'),
    url(r'^librarians$', list_librarians, name='list_librarians'),
    url(r'accounts/', include('django.contrib.auth.urls')),
]
