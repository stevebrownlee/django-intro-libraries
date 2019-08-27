import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from libraryapp.models import model_factory
from ..connection import Connection

def librarian_factory():
    def create(cursor, row):
        instance = Librarian()

        smart_row = sqlite3.Row(cursor, row)
        for col in smart_row.keys():
            setattr(instance, col, smart_row[col])
        return instance
    return create


def get_librarian(library_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                l.id,
                u.first_name,
                u.last_name,
                u.email
            FROM libraryapp_librarian l
            JOIN auth_user u ON l.user_id = u.id
            WHERE l.id = ?
            """, (library_id,)
        )

        return db_cursor.fetchone()

def get_librarians():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                l.id,
                u.first_name,
                u.last_name,
                u.email
            FROM libraryapp_librarian l
            JOIN auth_user u ON l.user_id = u.id
        """)

        return db_cursor.fetchall()


@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':

        librarian = get_librarian(librarian_id)
        template = 'librarians/detail.html'
        context = {
            'librarian': librarian
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a library
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM libraryapp_librarian
                    WHERE id = ?
                """, (librarian_id,))

            return redirect(reverse('libraryapp:librarians'))
