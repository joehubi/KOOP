import os
import sys
from enum import Enum

# Sicherstellen, dass das Skript im richtigen Kontext läuft
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_list.settings')

import django
django.setup()
from mylist.models import Members


def create_member_enum():
    # Alle Members aus der DB holen, sortiert nach name_nr
    members = Members.objects.all().order_by('name_nr')
    # Enum-Einträge als Tupel (NAME, Wert)
    enum_entries = []
    for idx, member in enumerate(members):
        # Enum-Namen generieren: Großbuchstaben, Leerzeichen und Sonderzeichen ersetzen
        enum_name = member.name.upper().replace(' ', '_').replace('/', '_').replace('&', 'UND').replace('Ä', 'AE').replace('Ö', 'OE').replace('Ü', 'UE').replace('ß', 'SS')
        enum_entries.append((enum_name, idx))
    # Enum dynamisch erzeugen
    return Enum('MemberEnum', enum_entries)

# Beispiel für die Verwendung:
MemberEnum = create_member_enum()

# Zugriff:
for member in MemberEnum:
    print(member.name, member.value)  # Enum-Name, Wert (beginnend bei 0)