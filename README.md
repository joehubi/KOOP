# Installation

1. Environment erstellen lassen
        python -m venv venv  
2. Environment aktivieren
* Windows: "./venv/Scripts/activate"
* Linux: source venv/bin/activate
4. Django installieren
        pip install Django
5. Alle HTML müssen initialisiert / erstellt werden mit dem Skript create_html_clones.py im Ordner HTML
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


# Runserver Startdatei unter Linux

Beispiel:
* Projektordner: /home/user/Koop/KOOP-main
* venv: /home/user/Koop/KOOP-main/venv
* manage.py: /home/user/Koop/KOOP-main/manage.py

## Schritt 1: Shell-Skript (start_django.sh)
        nano /home/user/Koop/KOOP-main/start_django.sh

### Inhalt des Shell-Skript (start)
        #!/bin/bash

### ins Projektverzeichnis wechseln
        cd /home/user/Koop/KOOP-main

### venv aktivieren
        source venv/bin/activate

### Django Server starten
        python manage.py runserver 0.0.0.0:8000

Speichern: CTRL+O → Enter → CTRL+X

### Inhalt des Shell-Skript (ende)

### Ausführbar machen:
        chmod +x /home/user/Koop/KOOP-main/start_django.sh

## Schritt 2: Desktop-Verknüpfung erstellen
        nano ~/Desktop/KOOP-server.desktop

### Inhalt:
        [Desktop Entry]
        Type=Application
        Name=KOOP Django Server
        Exec=lxterminal -e "/home/user/Koop/KOOP-main/start_django.sh"
        Icon=utilities-terminal
        Terminal=true

### Speichern und ausführbar machen:
        chmod +x ~/Desktop/KOOP-server.desktop

# Allgemein Django Projekt erstellen

1. Django installieren:             python -m pip install Django
2. Projekt "shopping_list" starten  
        . = im selben Ordner
        django-admin startproject shopping_list .
3. App erstellen (erstellt python files)
        python manage.py startapp mylist
