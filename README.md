# KOOP

## PreInstallation

1. Django installieren:             python -m pip install Django
2. Projekt "shopping_list" starten  
        . = im selben Ordner
        django-admin startproject shopping_list .
3. App erstellen (erstellt python files)
        python manage.py startapp mylist


## Lokales Repositor erstellen

1. Environment erstellen lassen
        python -m venv env  
2. Environment aktivieren
        "./env/Scripts/activate"
3. Django installieren
        pip install Django
4. Aus den Models den SQL Code erstellen
        python manage.py makemigrations
5. SQL auf der Datenbank ausführen
        python manage.py migrate
6. User im Admin-Bereich anlegen
        python manage.py createsuperuser
7. Server starten
        python manage.py runserver


## HTML

Alle HTML Koop_1.html bis Koop_15.html sind identisch!!!!