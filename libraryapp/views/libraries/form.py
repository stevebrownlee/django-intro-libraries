import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


def get_library(library_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.title,
            l.address
        FROM libraryapp_library l
        WHERE l.id = ?
        """, (library_id,))

    return db_cursor.fetchone()


@login_required
def library_form(request):
    if request.method == 'GET':
        template = 'libraries/form.html'
        context = {}

        return render(request, template, context)


@login_required
def library_edit_form(request, library_id):
    if request.method == 'GET':
        library = get_library(library_id)

        template = 'libraries/form.html'
        context = {
            'library': library
        }

        return render(request, template, context)
