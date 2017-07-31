# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from project.apps.books.helpers import create_super_user, create_books


def create_super_user_and_books(apps, schema_editor):
	create_super_user()
	create_books()


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_super_user_and_books)
    ]
