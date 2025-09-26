# region IMPORT
from django.shortcuts import render
from django.db.models import Sum
import csv
from .forms import CSVUploadForm
import re
from datetime import datetime
from collections import Counter

from .models import Person1
from .models import Person2
from .models import Person3
from .models import Person4
from .models import Person5
from .models import Person6
from .models import Person7
from .models import Person8
from .models import Person9
from .models import Person10
from .models import Person11
from .models import Person12
from .models import Person13
from .models import Person14
from .models import Person15

from .models import PriceList
from .models import Members
from .models import Konto
from .models import Save
# endregion

# region Definitions
first_person = 1
last_person = 15
# endregion

# region Finanzdienst
def finanzdienst(request):

    if request.method == 'POST':
        print("Alle abrechnen")

        for i in range(first_person, last_person): 
            person_model = get_person_model(i) 
            instances = person_model.objects.filter(done=False)
            instances.update(done=True)

    return render(request, 'finanzdienst.html', {})

def sum_and_book_all(request):

    if request.method == 'POST':

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
                Konto.objects.create(cashflow=-1*gesamte_euro_summe, nr=nr, comment='Koop-Einkauf')

                # Alle Einträge in der Person-Datenbank auf done=True setzen
                person_model = get_person_model(nr) 
                instances = person_model.objects.filter(done=False)
                instances.update(done=True)

                print(f"Koop-Einkauf verbucht für {member['name']} mit {gesamte_euro_summe} Euro.")

            print("Alle Summen wurden erfolgreich verbucht.")

    return render(request, 'finanzdienst.html', {})

def pay_rent(request):

    if request.method == 'POST':
        print("Miete abbuchen")

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

    return render(request, 'finanzdienst.html', {})
# endregion

# region CSV Import
def convert_date_format(date_str):
    try:
        # Konvertiere das Datum vom Format 'TT.MM.JJJJ' zu 'YYYY-MM-DD'
        return datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')
    except ValueError:
        # Falls das Datum nicht im erwarteten Format ist, Fehler ausgeben
        print(f'{date_str} has an invalid format. Please use DD.MM.YYYY format.')
        raise Exception(f'Invalid date format: {date_str}')

def import_csv(request):

    daten1 = PriceList.objects.all().order_by('name')
    daten2 = PriceList.objects.all().order_by('price')

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8')
            csv_data = csv.reader(csv_file.splitlines(), delimiter=";")
            
            for i, row_value in enumerate(csv_data):

                row_value[5] = convert_date_format(row_value[5])    # convert date from .csv to django-timestamp

                # Testausgabe
                print(f"i = {i}")
                print(f"Column1 = {row_value[0]}")
                print(f"Column2 = {row_value[1]}")

                # Eintrag in Datenbank erstellen aus der .csv-Datei
                PriceList.objects.create(
                    article_number = row_value[0],           # Entsprechend der Anordung in der .csv Datei
                    category = row_value[1],
                    name = row_value[2],
                    price = row_value[3],
                    type = row_value[4],
                    delivery_date = row_value[5],
                    status = row_value[6],
                )

    else:
        form = CSVUploadForm()

    return render(request, 'import_csv.html', {'form': form, 'daten1': daten1, 'daten2': daten2})
# endregion

# region Konto
# Hier werden Konto-Buchungen definiert. So können Koop-Einzahlungen, Miete etc. erfasst werden. 
def konto_add(request):

    if request.method == 'POST':
        nameNr = request.POST.get('nameNr', None)
        print('Konto:', nameNr)
        eintrag = Save.objects.get(id=1)    # Referenz zur Datenbank (Der Zwischenspeicher ist statisch immer auf der 1)
        eintrag.nr_save = nameNr            
        eintrag.save()                      # Änderungen in Member-Datenbank speichern

    nameNr = Save.objects.get(id=1)        # Nummer aus DB holen (Der Zwischenspeicher ist statisch immer auf der 1)
    print('Load:', nameNr.nr_save)

    if nameNr.nr_save == 0:
        all_items = Konto.objects.all()
        Aktueller_Name = ""
    else:
        all_items = Konto.objects.filter(nr = nameNr.nr_save).order_by('-created_at')
        Aktueller_Name = Members.objects.filter(name_nr=nameNr.nr_save).values('name').first()['name']

    # Summe der cashflow-Spalte berechnen
    summe_cashflow = all_items.aggregate(Sum('cashflow'))['cashflow__sum']                  

    if summe_cashflow is not None:
        eintrag = Save.objects.get(id=1)    
        eintrag.sum_save = summe_cashflow            
        eintrag.save()    
        print("Die Summe der cashflow-Werte beträgt:", summe_cashflow)
    else:
        print("Es wurden keine Datensätze gefunden oder die cashflow-Spalte enthält NULL-Werte.")
        
    all_Saves = Save.objects.all()    
    memberdaten = Members.objects.all()

    # passing the data to the HTML
    return render(request, 'Koop_konto.html', {'all_items': all_items, 'all_saves': all_Saves, 'memberdaten': memberdaten, 'Aktueller_Name': Aktueller_Name})

def konto_add2(request):

    if request.method == 'POST':
        Konto.objects.create(name = request.POST['itemName'], cashflow = request.POST['itemAmount'], nr = request.POST['itemNr'], comment = request.POST['itemComment'])
        printname = request.POST['itemName'] + '---' + request.POST['itemAmount'] + ' €' + '--- [' + request.POST['itemNr'] + ' ]' + ' [' + request.POST['itemComment'] + ' ]'
        print('Betrag hinzufügen:', printname)
    all_items = Konto.objects.all()
    all_Saves = Save.objects.all()

    return render(request, 'Koop_konto.html', {'all_items': all_items, 'all_saves': all_Saves})
# endregion

# region Einkauf/Person 
# Hier wird definiert welche Ansichten und Funktionen für einen Einkauf (Person X) zur Verfügung stehen

# Artikel hinzufügen/einkaufen
def add_person(request, person_id):
    if request.method == 'POST':
        name    = request.POST['itemName']
        amount  = request.POST['itemAmount']
        price   = request.POST['itemPrice']
        
        # Erstellen Sie das Person-Objekt basierend auf der übergebenen Personen-ID
        person_model = get_person_model(person_id)
        
        # Erstellen Sie das Objekt in der Datenbank
        person_model.objects.create(name=name, amount=amount, price=price)
        
        printname = f"{name}---{amount} kg/Stk ---{price} €"
        print('Hinzufügen (manuell):', printname)
    
    all_items = get_person_model(person_id).objects.filter(done=False).order_by('-id')
    
    all_members = Members.objects.all()

    preise_frischware   = PriceList.objects.filter(category="Frischwaren", status=True).order_by('name')
    preise_obst         = PriceList.objects.filter(category="Obst", status=True).order_by('name')
    preise_gemuese      = PriceList.objects.filter(category="Gemüse", status=True).order_by('name')
    preise_fleisch      = PriceList.objects.filter(category="Fleisch", status=True).order_by('name')
    preise_getraenke    = PriceList.objects.filter(category="Getränke", status=True).order_by('name')
    preise_tiefkuehl    = PriceList.objects.filter(category="Tiefkühl", status=True).order_by('name')

    #member = Members.objects.get(id=person_id)
    member = Members.objects.get(name_nr=person_id)
    page_membername = member.name   # Übergibt die Werte an die HTML
    page_color = member.color       # Übergibt die Werte an die HTML
    page_sum = member.sum           # Übergibt die Werte an die HTML
    Nr_id = person_id               # Übergibt die Werte an die HTML
    page_persons = member.persons

    return render(request, f'koop_{person_id}.html',
                  {'all_items': all_items,
                    'all_members': all_members,
                    'page_membername': page_membername,
                    'page_persons': page_persons,
                    'page_color': page_color,
                    'page_sum': page_sum,
                    'Nr_id': Nr_id, 'preise_frischware': preise_frischware,
                    'preise_obst': preise_obst,
                    'preise_gemuese': preise_gemuese,
                    'preise_fleisch': preise_fleisch,
                    'preise_getraenke': preise_getraenke,
                    'preise_tiefkuehl': preise_tiefkuehl})

# Löschen eines Einkaufs/Artikels aus der Liste
def delete_person(request, person_id):
    if request.method == 'POST':
        item_number = request.POST['itemNumber']
        what_to_delete = get_person_model(person_id).objects.get(id=item_number)
        print('Lösche:', what_to_delete)
        what_to_delete.delete()
    
    return render(request, f'koop_{person_id}.html')

# Bilden der Summe des aktuellen Einkaufs
def sum_person(request, person_id):
    if request.method == 'POST':
        alle_eintraege = get_person_model(person_id).objects.filter(done=False)
        gesamte_euro_summe = sum(entry.price * entry.amount for entry in alle_eintraege)
        gesamte_euro_summe = round(gesamte_euro_summe, 2)
        print('Summe:', gesamte_euro_summe)
        eintrag = Members.objects.get(name_nr=person_id)     # Referenz zur Member-Datenbank
        eintrag.sum = gesamte_euro_summe                # Summe holen
        eintrag.save()                                  # Änderungen in Member-Datenbank speichern

    return render(request, f'koop_{person_id}.html')
# endregion

# region Aufruf der Funktionen für einen Einkauf
# region Funktion zum Zuordnen der Namen
def get_person_model(person_id):
    # Hier können Sie die Zuordnung zwischen Personen-ID und Datenbankmodell implementieren
    # Zum Beispiel: Person 1 -> Person1, Person 2 -> Person2 usw.
    # Diese Funktion sollte das entsprechende Datenbankmodell zurückgeben.
    if person_id == 1:
        return Person1
    elif person_id == 2:
        return Person2
    elif person_id == 3:
        return Person3
    elif person_id == 4:
        return Person4
    elif person_id == 5:
        return Person5
    if person_id == 6:
        return Person6
    elif person_id == 7:
        return Person7
    elif person_id == 8:
        return Person8
    elif person_id == 9:
        return Person9
    elif person_id == 10:
        return Person10
    elif person_id == 11:
        return Person11  
    elif person_id == 12:
        return Person12  
    elif person_id == 13:
        return Person13  
    elif person_id == 14:
        return Person14
    elif person_id == 15:
        return Person15                                               
    # Fügen Sie weitere Zuordnungen hinzu, falls erforderlich
    # Beispiel: elif person_id == 4: return Person4
    else:
        # Wenn keine Übereinstimmung gefunden wird, können Sie eine Ausnahme auslösen oder ein Standardmodell zurückgeben
        raise ValueError("Ungültige Personen-ID")
# endregion
# region Funktion für View erstellen
# Definiert einen View für jede Person
def Person_1_add(request):
    return add_person(request, 1)
def Person_1_addSmart(request):
    return add_person_smart(request, 1)
def Person_1_delete(request):
    return delete_person(request, 1)
def Person_1_sum(request):
    return sum_person(request, 1)
        
def Person_2_add(request):
    return add_person(request, 2)
def Person_2_addSmart(request):
    return add_person_smart(request, 2)
def Person_2_delete(request):
    return delete_person(request, 2)
def Person_2_sum(request):
    return sum_person(request, 2)        

def Person_3_add(request):
    return add_person(request, 3)
def Person_3_addSmart(request):
    return add_person_smart(request, 3)
def Person_3_delete(request):
    return delete_person(request, 3)
def Person_3_sum(request):
    return sum_person(request, 3)      

def Person_4_add(request):
    return add_person(request, 4)
def Person_4_addSmart(request):
    return add_person_smart(request, 4)
def Person_4_delete(request):
    return delete_person(request, 4)
def Person_4_sum(request):
    return sum_person(request, 4)      

def Person_5_add(request):
    return add_person(request, 5)
def Person_5_addSmart(request):
    return add_person_smart(request, 5)
def Person_5_delete(request):
    return delete_person(request, 5)
def Person_5_sum(request):
    return sum_person(request, 5)      

def Person_6_add(request):
    return add_person(request, 6)
def Person_6_addSmart(request):
    return add_person_smart(request, 6)
def Person_6_delete(request):
    return delete_person(request, 6)
def Person_6_sum(request):
    return sum_person(request, 6) 

def Person_7_add(request):
    return add_person(request, 7)
def Person_7_addSmart(request):
    return add_person_smart(request, 7)
def Person_7_delete(request):
    return delete_person(request, 7)
def Person_7_sum(request):
    return sum_person(request, 7) 

def Person_8_add(request):
    return add_person(request, 8)
def Person_8_addSmart(request):
    return add_person_smart(request, 8)
def Person_8_delete(request):
    return delete_person(request, 8)
def Person_8_sum(request):
    return sum_person(request, 8) 

def Person_9_add(request):
    return add_person(request, 9)
def Person_9_addSmart(request):
    return add_person_smart(request, 9)
def Person_9_delete(request):
    return delete_person(request, 9)
def Person_9_sum(request):
    return sum_person(request, 9) 

def Person_10_add(request):
    return add_person(request, 10)
def Person_10_addSmart(request):
    return add_person_smart(request, 10)
def Person_10_delete(request):
    return delete_person(request, 10)
def Person_10_sum(request):
    return sum_person(request, 10) 

def Person_11_add(request):
    return add_person(request, 11)
def Person_11_addSmart(request):
    return add_person_smart(request, 11)
def Person_11_delete(request):
    return delete_person(request, 11)
def Person_11_sum(request):
    return sum_person(request, 11) 

def Person_12_add(request):
    return add_person(request, 12)
def Person_12_addSmart(request):
    return add_person_smart(request, 12)
def Person_12_delete(request):
    return delete_person(request, 12)
def Person_12_sum(request):
    return sum_person(request, 12) 

def Person_13_add(request):
    return add_person(request, 13)
def Person_13_addSmart(request):
    return add_person_smart(request, 13)
def Person_13_delete(request):
    return delete_person(request, 13)
def Person_13_sum(request):
    return sum_person(request, 13) 

def Person_14_add(request):
    return add_person(request, 14)
def Person_14_addSmart(request):
    return add_person_smart(request, 14)
def Person_14_delete(request):
    return delete_person(request, 14)
def Person_14_sum(request):
    return sum_person(request, 14) 

def Person_15_add(request):
    return add_person(request, 15)
def Person_15_addSmart(request):
    return add_person_smart(request, 15)
def Person_15_delete(request):
    return delete_person(request, 15)
def Person_15_sum(request):
    return sum_person(request, 15) 
# endregion
# endregion

# region !!!NICHT AKTIV!!! Bestellungen
# Noch in der Testphase
def order_add(request):

    if request.method == 'POST':
        print('Call PDF2CSV')


        def extract_lines_with_numbers(text):
            lines = text.split('\n')
            extracted_lines = []
            for line in lines:
                if re.findall(r'^\s*\d{5,6}\b', line):  # Match lines starting with 5 or 6-digit numbers
                    extracted_lines.append(line.strip())   
            return extracted_lines

        def add_semicolon(text):
            # Define a regular expression pattern to match the desired format
            pattern = re.compile(r'(\d{5,6})\s+(\d+)\s+(.{15})\s+(.{5})\s+(.{31})\s+(.{14})\s+(.{7})\s+(.{8})')
            # Use re.sub to replace the matched pattern with the number followed by a semicolon
            modified_text = pattern.sub(r'\1;\2;\3;\4;\5;\6;\7;\8', text)       
            return modified_text

        pdf_path = 'C:\\Dev\\Rechnung.pdf'  # Update with your PDF file path
        output_file = 'C:\\Dev\\Lieferung.csv'

        # with open(pdf_path, 'rb') as file:
        #     pdf_reader = PdfReader(file)
        #     text = ''
        #     for page in pdf_reader.pages:
        #         text += page.extract_text()

        #     extracted_lines = extract_lines_with_numbers(text)

        #     with open(output_file, 'w') as output:
        #         for line in extracted_lines:
        #             line_added_semicolon = add_semicolon(line)
        #             output.write(line_added_semicolon + '\n')

    ActItems = Konto.objects.all()
    all_Saves = Save.objects.all()
    return render(request, 'Koop_Order.html', {'all_items': ActItems, 'all_saves': all_Saves})

# endregion
# region !!!NICHT AKTIV!!! Preisliste
def Koop_view_price_1(request):
    all_items = PriceList.objects.filter(category='Sonstige')
    all_items = all_items.order_by('name')
    return render(request, 'koop_price_1.html', {'all_items': all_items})

def Koop_view_price_2(request):
    all_items = PriceList.objects.filter(category='Frischware')
    all_items = all_items.order_by('name')
    return render(request, 'koop_price_2.html', {'all_items': all_items})

def Koop_view_price_3(request):
    all_items = PriceList.objects.filter(category='Gemüse')
    all_items = all_items.order_by('name')
    return render(request, 'koop_price_3.html', {'all_items': all_items})

def Koop_view_price_4(request):
    all_items = PriceList.objects.filter(category='Obst')
    all_items = all_items.order_by('name')
    return render(request, 'koop_price_4.html', {'all_items': all_items})

def Koop_view_price_5(request):
    all_items = PriceList.objects.all()
    all_items = all_items.order_by('category', 'name')
    return render(request, 'koop_price_5.html', {'all_items': all_items})
# endregion
# region !!!NICHT AKTIV!!! Personen
def add_person_smart(request, person_id):
    if request.method == 'POST':
        entry = PriceList.objects.get(id=request.POST['itemNumber'])
        print('Hinzufügen (aus Preisliste):', entry)
        
        # Erstellen Sie das Person-Objekt basierend auf der übergebenen Personen-ID
        person_model = get_person_model(person_id)
        
        # Erstellen Sie das Objekt in der Datenbank
        person_model.objects.create(name=entry.name, amount=request.POST['itemAmount'], price=entry.price)
    
    return render(request, f'koop_{person_id}.html')
#endregion
# region Debugging/Testing
# just for testing
def Testing_add(request):
    if request.method == 'POST':
        PriceList.objects.create(name = request.POST['itemName'], type = request.POST['itemType'], price = request.POST['itemPrice'])
        print('Hinzufügen Preisliste (Testing)')
    all_items = PriceList.objects.all()
    return render(request, 'testing.html', {'all_items': all_items})

# endregion
