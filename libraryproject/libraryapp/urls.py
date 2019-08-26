from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "libraryapp"
urlpatterns = [
    url(r'^$', book_list, name='books'),
    url(r'^books$', book_list, name='books'),
    url(r'^books/(?P<book_id>[0-9]+)$', book_details, name="book"),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
    url(r'^book/form$', book_form, name='book_form'),

    url(r'^libraries$', library_list, name='libraries'),
    url(r'^library/form$', library_form, name='library_form'),
    url(r'^libraries/(?P<library_id>[0-9]+)/form$', library_edit_form, name='library_edit_form'),
    url(r'^libraries/(?P<library_id>[0-9]+)$', library_details, name="library"),

    url(r'^librarians$', list_librarians, name='librarians'),

    url(r'accounts/', include('django.contrib.auth.urls')),
]
