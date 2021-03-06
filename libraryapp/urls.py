from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import *


app_name = "libraryapp"
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^books/(?P<book_id>[0-9]+)$', book_details, name="book"),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
    url(r'^book/form$', book_form, name='book_form'),

    url(r'^libraries$', library_list, name='libraries'),
    url(r'^libraries/(?P<library_id>[0-9]+)$', library_details, name="library"),
    url(r'^libraries/(?P<library_id>[0-9]+)/form$', library_edit_form, name='library_edit_form'),
    url(r'^library/form$', library_form, name='library_form'),

    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^librarians/(?P<librarian_id>[0-9]+)$', librarian_details, name="librarian"),

    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^register/$', register_user, name='register'),
]
