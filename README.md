# KOOP

## Installation

1. Environment erstellen lassen
        python -m venv venv  
2. Environment aktivieren
           Windows: "./venv/Scripts/activate"
           Linux: source venv/bin/activate
4. Django installieren
        pip install Django
5. Aus den Models den SQL Code erstellen
   python manage.py makemigrations
   Vorher die sqlite3 Datenbankdatei ins Verzeichnis kopieren        
7. SQL auf der Datenbank ausführen
        python manage.py migrate
8. User im Admin-Bereich anlegen
        python manage.py createsuperuser
9. Server starten
        python manage.py runserver


## HTML

Alle HTML Koop_1.html bis Koop_15.html sind identisch!!!!

## Allgemein Django Projekt erstellen

1. Django installieren:             python -m pip install Django
2. Projekt "shopping_list" starten  
        . = im selben Ordner
        django-admin startproject shopping_list .
3. App erstellen (erstellt python files)
        python manage.py startapp mylist
