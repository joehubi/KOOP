from django.db import models
from datetime import datetime 

# Create your models here.

# Preisliste

class PriceList(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    type = models.CharField(max_length=5)
    category = models.CharField(max_length=20, default='-')

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + str(self.price) + ' - ' + self.type + ' - ' + self.category

# Konto

class Konto(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nr = models.IntegerField(default=0)

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
        (9, '[9] -'),
        (10,'[10] Susanne Zehetmeier'),
        (11,'[11] Nora Siebels'),
        (12,'[12] Schürkämper'),
        (13,'[13] Gabi Mitschka'),
        (14,'[14] Fritz Spörl'),
    )
    
    nr = models.IntegerField(choices=NAME_CHOICES, default=0)
    
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
        return str(self.id) + ' - ' + str(self.created_at) + ' - ' + str(self.nr) + ' (Nr-Name)' + ' - ' + str(self.cashflow) + ' - ' + self.comment + ' - ' + self.comment2

# Save

class Save(models.Model):
    nr_save = models.IntegerField(default=0)
    sum_save = models.FloatField(default=0)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.nr_save) + ' - ' + str(self.sum_save)

# Member Liste

class Members(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=10)
    sum = models.FloatField(default=0)

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.color + ' - ' + str(self.sum)

# class Person

class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.done) + ' - ' + str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

    def calculate_total(self):
        total = self.amount * self.price
        return round(total, 2)

    class Meta:
        abstract = True

#
name1 = Members.objects.get(id=1+1)
name2 = Members.objects.get(id=2+1)
name3 = Members.objects.get(id=3+1)
name4 = Members.objects.get(id=4+1)
name5 = Members.objects.get(id=5+1)
name6 = Members.objects.get(id=6+1)
name7 = Members.objects.get(id=7+1)
name8 = Members.objects.get(id=8+1)
name9 = Members.objects.get(id=9+1)
name10 = Members.objects.get(id=10+1)
name11 = Members.objects.get(id=11+1)
name12 = Members.objects.get(id=12+1)
name13 = Members.objects.get(id=13+1)
name14 = Members.objects.get(id=14+1)
name15 = Members.objects.get(id=15+1)

# Personen

class Person1(Person):
    class Meta:
        db_table = 'mylist_person1'
        verbose_name = f'[1] {name1.name}'
        verbose_name_plural =  f'[1] {name1.name}'

class Person2(Person):
    class Meta:
        db_table = 'mylist_person2'
        verbose_name = f'[2] {name2.name}'
        verbose_name_plural =  f'[2] {name2.name}'

class Person3(Person):
    class Meta:
        db_table = 'mylist_person3'
        verbose_name = f'[3] {name3.name}'
        verbose_name_plural =  f'[3] {name3.name}'
      
class Person4(Person):
    class Meta:
        db_table = 'mylist_person4'
        verbose_name = f'[4] {name4.name}'
        verbose_name_plural =  f'[4] {name4.name}'
      
class Person5(Person):
    class Meta:
        db_table = 'mylist_person5'
        verbose_name = f'[5] {name5.name}'
        verbose_name_plural =  f'[5] {name5.name}'
      
class Person6(Person):
    class Meta:
        db_table = 'mylist_person6'
        verbose_name = f'[6] {name6.name}'
        verbose_name_plural =  f'[6] {name6.name}'
      
class Person7(Person):
    class Meta:
        db_table = 'mylist_person7'
        verbose_name = f'[7] {name7.name}'
        verbose_name_plural =  f'[7] {name7.name}'
      
class Person8(Person):
    class Meta:
        db_table = 'mylist_person8'
        verbose_name = f'[8] {name8.name}'
        verbose_name_plural =  f'[8] {name8.name}'
      
class Person9(Person):
    class Meta:
        db_table = 'mylist_person9'
        verbose_name = f'[9] {name9.name}'
        verbose_name_plural =  f'[9] {name9.name}'
      
class Person10(Person):
    class Meta:
        db_table = 'mylist_person10'
        verbose_name = f'[10] {name10.name}'
        verbose_name_plural =  f'[10] {name10.name}'
      
class Person11(Person):
    class Meta:
        db_table = 'mylist_person11'
        verbose_name = f'[11] {name11.name}'
        verbose_name_plural =  f'[11] {name11.name}'
    
class Person12(Person):
    class Meta:
        db_table = 'mylist_person12'
        verbose_name = f'[12] {name12.name}'
        verbose_name_plural =  f'[12] {name12.name}'
      
class Person13(Person):
    class Meta:
        db_table = 'mylist_person13'
        verbose_name = f'[13] {name13.name}'
        verbose_name_plural =  f'[13] {name13.name}'
      
class Person14(Person):
    class Meta:
        db_table = 'mylist_person14'
        verbose_name = f'[14] {name14.name}'
        verbose_name_plural =  f'[14] {name14.name}'
      
class Person15(Person):
    class Meta:
        db_table = 'mylist_person15'
        verbose_name = f'[15] {name15.name}'
        verbose_name_plural =  f'[15] {name15.name}'
      

"""
# Personen

class Person1(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.done) + ' - ' + str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person2(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.done) + ' - ' + str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person3(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.done) + ' - ' + str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name

class Person4(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.done) + ' - ' + str(self.id) + ' - ' + str(self.created_at) + ' - ' + self.name


"""
