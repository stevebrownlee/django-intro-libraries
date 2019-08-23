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
        '''
        Check if the request method is a GET, and if so, get all the
        libraries in the system so that the book form has a <select>
        element with all the libraries as <option> elements
        '''

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

        template_name = 'books/form.html'
        return render(request, template_name, {'all_libraries': all_libraries})

    elif request.method == 'POST':
        '''
        Check if the request method is a POST, which means the user
        filled out the form and clicked the submit button. Then extract
        all the form fields from the request, and assign those values
        to a new Book instance. Then invoke the `.save()` method to
        insert the data into the database.
        '''

        form_data = request.POST

        if "book_id" in form_data and int(form_data["book_id"]) > 0:
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE libraryapp_book
                SET title = ?,
                    author = ?,
                    isbn = ?,
                    year_published = ?,
                    location_id = ?
                WHERE id = ?
                """,
                    (
                        form_data['title'], form_data['author'],
                        form_data['isbn'], form_data['year_published'],
                        form_data["location"], form_data["book_id"],
                    )
                )

            return redirect(reverse('libraryapp:list_books'))

        else:
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                INSERT INTO libraryapp_book
                (title, author, isbn, year_published, location_id, librarian_id)
                values (?, ?, ?, ?, ?, ?)
                """,
                (form_data['title'], form_data['author'],
                    form_data['isbn'], form_data['year_published'],
                    request.user.librarian.id, form_data["location"]))

            return redirect(reverse('libraryapp:list_books'))
