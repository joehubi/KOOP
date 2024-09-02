

# Environment erstellen lassen
python -m venv env

# Environment aktivieren
"./env/Scripts/activate"

# Django installieren
python -m pip install Django

# Projekt "shopping_list" starten 
# . = im selben Ordner
django-admin startproject shopping_list .

# Server starten
python manage.py runserver

# App erstellen (erstellt python files)
python manage.py startapp mylist

# User im Admin-Bereich anlegen
python manage.py createsuperuser

# Aus den Models den SQL Code erstellen
python manage.py makemigrations

# SQL auf der Datenbank ausführen
python manage.py migrate

# Extensions für VisualCode
# SQLite + SQLite Viewer installieren


# Datenbank löschen (ID's zurücksetzen)
# Mit dem SQLite Tool

# DELETE FROM mylist_person1;
# DELETE FROM sqlite_sequence WHERE name='mylist_person1';

# ToDo's
#
# - 