"""Buchen der Summen (Test-Skript)
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
from mylist.views import get_person_model

print("Summen verbuchen")

# Alle Members mit allen Feldern holen
members = list(Members.objects.values('name_nr', 'persons', 'name'))
print("Alle Members (inkl. Duplikate):")
for member in members:
    print(member)

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
        if member["persons"] == 0:
            print(f"Member {member['name']} hat keine Personen, überspringe...")
            continue
        nr = member['name_nr']
        alle_eintraege = get_person_model(nr).objects.filter(done=False)
        gesamte_euro_summe = sum(entry.price * entry.amount for entry in alle_eintraege)
        gesamte_euro_summe = round(gesamte_euro_summe, 2)
        print(f"Summe: {gesamte_euro_summe}, Name: {member['name']}, Name Nr: {nr}")
        eintrag = Members.objects.get(name_nr=nr)     # Referenz zur Member-Datenbank
        eintrag.sum = gesamte_euro_summe                # Summe holen
        eintrag.save()                                  # Änderungen in Member-Datenbank speichern
        # Konto-Eintrag erstellen
        Konto.objects.create(cashflow=gesamte_euro_summe, nr=nr, comment='Koop-Einkauf')
        print(f'Koop-Einkauf verbucht für {member['name']} mit {gesamte_euro_summe} Euro.')
    print("Alle Summen wurden erfolgreich verbucht.")