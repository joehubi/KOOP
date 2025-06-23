# region   Import
from django.contrib import admin

from .models import PriceList
from .models import Members
from .models import Konto
from .models import Save
from .models import Warenliste

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
# endregion

# Entfernt die Standard-Aktion (LÖSCHEN)
admin.site.disable_action('delete_selected')

# User Aktion ABGERECHNET
def DONE_TRUE(modeladmin, request, queryset):
    queryset.update(done=True)
DONE_TRUE.short_description = "ABGERECHNET"

# User Aktion OFFEN
def DONE_FALSE(modeladmin, request, queryset):
    queryset.update(done=False)
DONE_FALSE.short_description = "OFFEN"

# User Aktion AKTUELL
def STATUS_TRUE(modeladmin, request, queryset):
    queryset.update(status=True)
STATUS_TRUE.short_description = "AKTUELL"

# User Aktion AUSSORTIERT
def STATUS_FALSE(modeladmin, request, queryset):
    queryset.update(status=False)
STATUS_FALSE.short_description = "AUSSORTIERT"

# User Aktion LÖSCHEN
def DELETE(modeladmin, request, queryset):
    queryset.delete()
DELETE.short_description = "LÖSCHEN"

# region Klassen
class Person1Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person2Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person3Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person4Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person5Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person6Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person7Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person8Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person9Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person10Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person11Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person12Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person13Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person14Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')
class Person15Admin(admin.ModelAdmin):
    actions = [DONE_TRUE, DONE_FALSE]
    list_display = ('id', 'done', 'created_at', 'name', 'amount','price')

class KontoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nr', 'created_at', 'cashflow', 'date', 'comment','comment2')

class WarenlisteAdmin(admin.ModelAdmin):
    list_display = ('id', 'artikelnummer', 'artikelname', 'sortiment', 'artikelname_neu')

class PriceListAdmin(admin.ModelAdmin):
    actions = [STATUS_TRUE, STATUS_FALSE]
    list_display = ('id','article_number' ,'delivery_date', 'status', 'name', 'price', 'type', 'category', 'created_at')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_nr', 'name', 'persons', 'color', 'sum')
# endregion

# region Register models
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(Members, MemberAdmin)
admin.site.register(Konto, KontoAdmin)
admin.site.register(Save)
admin.site.register(Warenliste, WarenlisteAdmin)

admin.site.register(Person1, Person1Admin)
admin.site.register(Person2, Person2Admin)
admin.site.register(Person3, Person3Admin)
admin.site.register(Person4, Person4Admin)
admin.site.register(Person5, Person5Admin)
admin.site.register(Person6, Person6Admin)
admin.site.register(Person7, Person7Admin)
admin.site.register(Person8, Person8Admin)
admin.site.register(Person9, Person9Admin)
admin.site.register(Person10, Person10Admin)
admin.site.register(Person11, Person11Admin)
admin.site.register(Person12, Person12Admin)
admin.site.register(Person13, Person13Admin)
admin.site.register(Person14, Person14Admin)
admin.site.register(Person15, Person15Admin)
# endregion