import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


@login_required
def create_book(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address
            from libraryapp_library l
            """)

            all_libraries = db_cursor.fetchall()

        template_name = 'books/create.html'
        return render(request, template_name, {'all_libraries': all_libraries})

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address
            from libraryapp_library l
            where l.id = ?
            """, form_data["location"])

            library = db_cursor.fetchone()

        new_book = Book(
            librarian=request.user.librarian,
            title=form_data['title'],
            author=form_data['author'],
            isbn=form_data['isbn'],
            year_published=form_data['year_published'],
            location=library,
        )
        new_book.save()

        return redirect(reverse('libraryapp:list_books'))
