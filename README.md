# Installation

git clone "dieses Repo"

1. Environment erstellen lassen
* python -m venv venv  
2. Environment aktivieren
* Windows: "./venv/Scripts/activate"
* Linux: source venv/bin/activate
4. Django installieren
* pip install Django
5. Alle HTML müssen initialisiert / erstellt werden
* mit dem Skript create_html_clones.py im Ordner HTML
* python create_html_clones.py
6. Aus den Models den SQL Code erstellen
* python manage.py makemigrations
* Vorher die sqlite3 Datenbankdatei ins Verzeichnis kopieren        
7. SQL auf der Datenbank ausführen
* python manage.py migrate
8. User im Admin-Bereich anlegen
* python manage.py createsuperuser
9. Server starten
* python manage.py runserver

# Django Benutzer anlegen
python manage.py createsuperuser
   

# Runserver Startdatei unter Linux

Beispiel:
* Projektordner: /home/user/Koop/KOOP
* venv: /home/user/Koop/KOOP/venv
* manage.py: /home/user/Koop/KOOP/manage.py

## Ausführbar machen unter Linux:
        chmod +x /home/user/Koop/KOOP/start_django.sh

## Schritt 2: Desktop-Verknüpfung erstellen
Datei "KOOP-server.desktop" aus Verzeichnis auf Desktop kopieren 

### Speichern und ausführbar machen:
        chmod +x ~/Desktop/KOOP-server.desktop

# Allgemein Django Projekt erstellen

1. Django installieren:             python -m pip install Django
2. Projekt "shopping_list" starten  
        . = im selben Ordner
        django-admin startproject shopping_list .
3. App erstellen (erstellt python files)
        python manage.py startapp mylist
