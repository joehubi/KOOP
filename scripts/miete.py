"""Abbuchen der Miete (Test-Skript)
"""
import os
import sys

# Sicherstellen, dass das Skript im richtigen Kontext läuft
# Hier wird der Pfad zum Django-Projekt gesetzt, damit die Modelle importiert werden können
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_list.settings')

# Setzen der Django-Einstellungen
# Dies ist notwendig, um Django-Modelle zu verwenden
import django
django.setup()
from collections import Counter
from mylist.models import Members, Konto, Save

# Miete auslesen
save_object = Save.objects.get(id=1)
miete = save_object.rent_save
print(f"Miete ({miete} €) pro Person abbuchen")

# Alle Members mit allen Feldern holen
members = list(Members.objects.values('name_nr', 'persons'))
print("Alle Members (inkl. Duplikate):", members)

# Prüfen, ob name_nr unique ist
name_nr_list = [m['name_nr'] for m in members]
counter = Counter(name_nr_list)
duplicates = [nr for nr, count in counter.items() if count > 1]
if duplicates:
    print(f"Fehler: Die folgenden name_nr-Werte sind nicht eindeutig: {duplicates}")
else:
    print("Alle name_nr-Werte sind eindeutig.")

    # Für jeden Member cashflow berechnen und Konto-Eintrag erstellen
    for member in members:
        nr = member['name_nr']
        persons = member['persons']
        miete_total_persons = miete * persons
        print(f'Miete abbuchen für: {nr} ({persons} Personen, cashflow={miete_total_persons})')
        Konto.objects.create(cashflow=(-miete_total_persons), nr=nr, comment='Miete')
    print("Alle Miete-Einträge wurden erfolgreich erstellt.")