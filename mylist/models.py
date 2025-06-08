# region IMPORT
from django.db import models
import datetime 
# endregion

# region Preisliste
# Modell für die Preislisten. Wird noch nicht aktiv verwendet

class PriceList(models.Model):
    name = models.CharField(max_length=200)     # Artikelname
    price = models.FloatField(default=0)        # in €

    NAME_CHOICES1 = (
        ("Stk", "Stk"),
        ("kg",  "kg"),
        ("Pfand", "Pfand"),
    )
    NAME_CHOICES2 = (
        ("Obst", "Obst"),
        ("Gemüse",  "Gemüse"),
        ("Frischwaren",  "Frischwaren"),
        ("Fleisch",  "Fleisch"),
        ("Getränke",  "Getränke"),
        ("Tiefkühl",  "Tiefkühl"),
    )

    created_at = models.DateTimeField(auto_now_add=True)                            # Zeitstempel
    type = models.CharField(choices=NAME_CHOICES1, max_length=5)                    # Stk, kg, Pfand
    category = models.CharField(choices=NAME_CHOICES2, max_length=20, default='-')  # Kategorie/Preisart/Sortiment
    status = models.BooleanField(default=True)                                      # true = neuer oder aktueller Artikel, false = Artikel nicht mehr aktuell im Sortiment vorhanden
    article_number = models.IntegerField(default=0)
    delivery_date = models.DateField(default='10.10.1999')                      # Lieferdatum

    def __str__(self):
        return  str(self.status) + ' - ' + str(self.id) + ' - ' + self.name + ' - ' + str(self.price) + ' - ' + self.type + ' - ' + self.category
# endregion

# region Konto
# Definiert einen Konto-Eintrag.
# Die Namensliste zur Bearbeitung in der ADMIN-Ansicht ist hier lokal definiert. Das ist noch ein nachteil im Code.

class Konto(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.date.today)  # Datum des Eintrags
    # nr = models.IntegerField(default=0)

    NAME_CHOICES = (
        (0, '-'),
        (1, '[1] Huber/Hoffmann'),
        (2, '[2] Teßmann'),
        (3, '[3] Wenninger/Fiedler'),
        (4, '[4] Sonja Gartner'),
        (5, '[5] Hildegund & Osi'),
        (6, '[6] Sarita Schwerla'),
        (7, '[7] Laux'),
        (8, '[8] Klaus Plessner'),
        (9, '[9] Koller'),
        (10,'[10] Susanne Zehetmeier'),
        (11,'[11] Nora Siebels'),
        (12,'[12] Schürkämper'),
        (13,'[13] Gabi Mitschka'),
        (14,'[14] Fritz Spörl'),
    )
    
    # nr = models.IntegerField(choices=NAME_CHOICES, default=0)
    nr = models.IntegerField(choices=NAME_CHOICES, default=0, unique=True)
    
    cashflow = models.FloatField(default=0)

    COMMENT_CHOICES = (
        ('Einzahlung', 'Einzahlung'),
        ('Miete', 'Miete'),
        ('Koop-Einkauf', 'Koop-Einkauf'),
        ('Sonstiges', 'Sonstiges'),
    )
    comment = models.CharField(choices=COMMENT_CHOICES, max_length=200)
    comment2 = models.CharField(max_length=200, default='-')

    def __str__(self):
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + str(self.nr) + ' (Nr-Name)' + ' - ' + str(self.cashflow) + ' - ' + str(self.date) + ' - ' + self.comment + ' - ' + self.comment2
# endregion

# region Save
# Definiert eine Zwischenablage zur Speicherung der SUMMEN
class Save(models.Model):
    nr_save = models.IntegerField(default=0)
    sum_save = models.FloatField(default=0)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.nr_save) + ' - ' + str(self.sum_save)
# endregion

# region Member Liste
# Definiert wie ein Member-Eintrag auszusehen hat.
# Empfehlung color: Google Color picker
class Members(models.Model):
    name    = models.CharField(max_length=200)
    color   = models.CharField(max_length=10)
    sum     = models.FloatField(default=0)
    name_nr = models.IntegerField(default=0)
    persons = models.IntegerField(default=1)  # Anzahl der Personen, die zu diesem Member gehören

    def __str__(self):
        return str(self.id) + ' - ' + self.name + '-' + str(self.persons) + ' - ' + self.color + ' - ' + str(self.sum)
# endregion 

# region Person/Einkauf
# Definiert wie eine Person einkaufen kann.
class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)    # Zeitstempel
    name = models.CharField(max_length=200)     # Name des Produktes/Artikels
    amount = models.FloatField(default=0)       # Menge in Stk oder kg
    price = models.FloatField(default=0)        # Preis in €
    done = models.BooleanField(default=False)   # Wird zur Abrechnung (Finanzdienst) verwendet. 0=nicht gebucht, 1=gebucht auf Konto (wird nicht mehr in der aktuellen Liste dargestellt)

    def __str__(self):
        return str(self.done) + ' - ' + str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

    def calculate_total(self):
        total = self.amount * self.price
        return round(total, 2)

    class Meta:
        abstract = True
# endregion

# region Warenliste

class Warenliste(models.Model):
    artikelnummer = models.IntegerField(default=0)     # Artikelnummer von Ökoring
    artikelname = models.CharField(max_length=200)     # Artikelname der bei Ökoring auf der Rechnung steht
    sortiment = models.CharField(max_length=200)       # Sortiment = Kategorie (Fleisch, Obst, etc.)
    artikelname_neu = models.CharField(max_length=200) # Dieser Name wird dann in der Preisliste angezeigt

    def __str__(self):
        return str(self.id) + '-' + str(self.artikelnummer) + ' - ' + self.artikelname + ' - ' + self.sortiment + '-' + self.artikelname_neu
# endregion

# region Members
# region DB MANIPULATION

# Datenbank Konfiguration
# Damit der nachfolgende Code funktional wird und es zu keinen Fehlern bei makemigrations/migrate kommt, muss die 
# Datenbank korrekt eingerichtet werden. Damit ist im speziellen gemeint, dass eine Tabelle mylist_members mit
# mindestens 15 Einträgen vorhanden sein muss.

# Am Anfang bei Einrichtung der Datenbank/Django einkommentieren

name1 = 'Huber/Hoffmann'
name2 = 'Teßmann'
name3 = 'Wenninger/Fiedler'
name4 = 'Sonja Gartner'
name5 = 'Hildegund & Osi'
name6 = 'Sarita Schwerla'
name7 = 'Laux'
name8 = 'Klaus Plessner'
name9 = 'Koller'
name10 = 'Susanne Zehetmeier'
name11 = 'Nora Siebels'
name12 = 'Schürkämper'
name13 = 'Gabi Mitschka'
name14 = 'Fritz Spörl'
name15 = '-'

# Am Anfang bei Einrichtung der Datenbank/Django auskommentieren
# Das ist leider notwendig, da dieser Code zu einem Fehler führt, solange die DB nicht vorhanden ist.
# name1 = Members.objects.get(name_nr=1)
# name2 = Members.objects.get(name_nr=2)
# name3 = Members.objects.get(name_nr=3)
# name4 = Members.objects.get(name_nr=4)
# name5 = Members.objects.get(name_nr=5)
# name6 = Members.objects.get(name_nr=6)
# name7 = Members.objects.get(name_nr=7)
# name8 = Members.objects.get(name_nr=8)
# name9 = Members.objects.get(name_nr=9)
# name10 = Members.objects.get(name_nr=10)
# name11 = Members.objects.get(name_nr=11)
# name12 = Members.objects.get(name_nr=12)
# name13 = Members.objects.get(name_nr=13)
# name14 = Members.objects.get(name_nr=14)
# name15 = Members.objects.get(name_nr=15)
# endregion

# region Personen/Members
# Definiert die personen-Tabellen in der DB. Jede Person hat eine Tabelle.
class Person1(Person):
    class Meta:
        db_table = 'mylist_person1'
        verbose_name = f'[1] {name1}'
        verbose_name_plural =  f'[1] {name1}'

class Person2(Person):
    class Meta:
        db_table = 'mylist_person2'
        verbose_name = f'[2] {name2}'
        verbose_name_plural =  f'[2] {name2}'

class Person3(Person):
    class Meta:
        db_table = 'mylist_person3'
        verbose_name = f'[3] {name3}'
        verbose_name_plural =  f'[3] {name3}'
      
class Person4(Person):
    class Meta:
        db_table = 'mylist_person4'
        verbose_name = f'[4] {name4}'
        verbose_name_plural =  f'[4] {name4}'
      
class Person5(Person):
    class Meta:
        db_table = 'mylist_person5'
        verbose_name = f'[5] {name5}'
        verbose_name_plural =  f'[5] {name5}'
      
class Person6(Person):
    class Meta:
        db_table = 'mylist_person6'
        verbose_name = f'[6] {name6}'
        verbose_name_plural =  f'[6] {name6}'
      
class Person7(Person):
    class Meta:
        db_table = 'mylist_person7'
        verbose_name = f'[7] {name7}'
        verbose_name_plural =  f'[7] {name7}'
      
class Person8(Person):
    class Meta:
        db_table = 'mylist_person8'
        verbose_name = f'[8] {name8}'
        verbose_name_plural =  f'[8] {name8}'
      
class Person9(Person):
    class Meta:
        db_table = 'mylist_person9'
        verbose_name = f'[9] {name9}'
        verbose_name_plural =  f'[9] {name9}'
      
class Person10(Person):
    class Meta:
        db_table = 'mylist_person10'
        verbose_name = f'[10] {name10}'
        verbose_name_plural =  f'[10] {name10}'
      
class Person11(Person):
    class Meta:
        db_table = 'mylist_person11'
        verbose_name = f'[11] {name11}'
        verbose_name_plural =  f'[11] {name11}'
    
class Person12(Person):
    class Meta:
        db_table = 'mylist_person12'
        verbose_name = f'[12] {name12}'
        verbose_name_plural =  f'[12] {name12}'
      
class Person13(Person):
    class Meta:
        db_table = 'mylist_person13'
        verbose_name = f'[13] {name13}'
        verbose_name_plural =  f'[13] {name13}'
      
class Person14(Person):
    class Meta:
        db_table = 'mylist_person14'
        verbose_name = f'[14] {name14}'
        verbose_name_plural =  f'[14] {name14}'
      
class Person15(Person):
    class Meta:
        db_table = 'mylist_person15'
        verbose_name = f'[15] {name15}'
        verbose_name_plural =  f'[15] {name15}'

# endregion
