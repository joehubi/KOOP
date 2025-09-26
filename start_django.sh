# Inhalt des Shell-Skript (start)
#!/bin/bash

# ins Projektverzeichnis wechseln
cd /home/user/Koop/KOOP-main

# venv aktivieren
source venv/bin/activate

# Django Server starten
python manage.py runserver 0.0.0.0:8000
