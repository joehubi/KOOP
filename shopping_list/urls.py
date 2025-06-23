"""
URL configuration for shopping_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# region IMPORT
from django.contrib import admin
from django.urls import path

from mylist.views import Testing_add

from mylist.views import order_add
from mylist.views import import_csv
from mylist.views import konto_add
from mylist.views import konto_add2
from mylist.views import finanzdienst
from mylist.views import pay_rent
from mylist.views import sum_and_book_all

from mylist.views import Koop_view_price_1
from mylist.views import Koop_view_price_2
from mylist.views import Koop_view_price_3
from mylist.views import Koop_view_price_4
from mylist.views import Koop_view_price_5

from mylist.views import Person_1_add
from mylist.views import Person_1_addSmart
from mylist.views import Person_1_delete
from mylist.views import Person_1_sum

from mylist.views import Person_2_add
from mylist.views import Person_2_addSmart
from mylist.views import Person_2_delete
from mylist.views import Person_2_sum

from mylist.views import Person_3_add
from mylist.views import Person_3_addSmart
from mylist.views import Person_3_delete
from mylist.views import Person_3_sum

from mylist.views import Person_4_add
from mylist.views import Person_4_addSmart
from mylist.views import Person_4_delete
from mylist.views import Person_4_sum

from mylist.views import Person_5_add
from mylist.views import Person_5_addSmart
from mylist.views import Person_5_delete
from mylist.views import Person_5_sum

from mylist.views import Person_6_add
from mylist.views import Person_6_addSmart
from mylist.views import Person_6_delete
from mylist.views import Person_6_sum

from mylist.views import Person_7_add
from mylist.views import Person_7_addSmart
from mylist.views import Person_7_delete
from mylist.views import Person_7_sum

from mylist.views import Person_8_add
from mylist.views import Person_8_addSmart
from mylist.views import Person_8_delete
from mylist.views import Person_8_sum

from mylist.views import Person_9_add
from mylist.views import Person_9_addSmart
from mylist.views import Person_9_delete
from mylist.views import Person_9_sum

from mylist.views import Person_10_add
from mylist.views import Person_10_addSmart
from mylist.views import Person_10_delete
from mylist.views import Person_10_sum

from mylist.views import Person_11_add
from mylist.views import Person_11_addSmart
from mylist.views import Person_11_delete
from mylist.views import Person_11_sum

from mylist.views import Person_12_add
from mylist.views import Person_12_addSmart
from mylist.views import Person_12_delete
from mylist.views import Person_12_sum

from mylist.views import Person_13_add
from mylist.views import Person_13_addSmart
from mylist.views import Person_13_delete
from mylist.views import Person_13_sum

from mylist.views import Person_14_add
from mylist.views import Person_14_addSmart
from mylist.views import Person_14_delete
from mylist.views import Person_14_sum

from mylist.views import Person_15_add
from mylist.views import Person_15_addSmart
from mylist.views import Person_15_delete
from mylist.views import Person_15_sum
# endregion

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Testing/add/', Testing_add),
    path('import/', import_csv),
    path('finanzdienst/', finanzdienst),
    path('finanzdienst/pay_rent', pay_rent),
    path('finanzdienst/sum_and_book_all', sum_and_book_all),
    
    path('Order/add/', order_add),

    path('Konto/add/', konto_add),
    path('Konto/add2/', konto_add2),

    path('koop_price_1/', Koop_view_price_1),
    path('koop_price_2/', Koop_view_price_2),
    path('koop_price_3/', Koop_view_price_3),
    path('koop_price_4/', Koop_view_price_4),
    path('koop_price_5/', Koop_view_price_5),

    path('Person_1/add/',       Person_1_add),
    path('Person_1/delete/',    Person_1_delete),
    path('Person_1/addSmart/',  Person_1_addSmart),
    path('Person_1/sum/',       Person_1_sum),

    path('Person_2/add/',       Person_2_add),
    path('Person_2/delete/',    Person_2_delete),
    path('Person_2/addSmart/',  Person_2_addSmart),
    path('Person_2/sum/',       Person_2_sum),

    path('Person_3/add/',       Person_3_add),
    path('Person_3/delete/',    Person_3_delete),
    path('Person_3/addSmart/',  Person_3_addSmart),
    path('Person_3/sum/',       Person_3_sum),

    path('Person_4/add/',       Person_4_add),
    path('Person_4/delete/',    Person_4_delete),
    path('Person_4/addSmart/',  Person_4_addSmart),
    path('Person_4/sum/',       Person_4_sum),

    path('Person_5/add/',       Person_5_add),
    path('Person_5/delete/',    Person_5_delete),
    path('Person_5/addSmart/',  Person_5_addSmart),
    path('Person_5/sum/',       Person_5_sum),

    path('Person_6/add/',       Person_6_add),
    path('Person_6/delete/',    Person_6_delete),
    path('Person_6/addSmart/',  Person_6_addSmart),
    path('Person_6/sum/',       Person_6_sum),

    path('Person_7/add/',       Person_7_add),
    path('Person_7/delete/',    Person_7_delete),
    path('Person_7/addSmart/',  Person_7_addSmart),
    path('Person_7/sum/',       Person_7_sum),

    path('Person_8/add/',       Person_8_add),
    path('Person_8/delete/',    Person_8_delete),
    path('Person_8/addSmart/',  Person_8_addSmart),
    path('Person_8/sum/',       Person_8_sum),

    path('Person_9/add/',       Person_9_add),
    path('Person_9/delete/',    Person_9_delete),
    path('Person_9/addSmart/',  Person_9_addSmart),
    path('Person_9/sum/',       Person_9_sum),

    path('Person_10/add/',       Person_10_add),
    path('Person_10/delete/',    Person_10_delete),
    path('Person_10/addSmart/',  Person_10_addSmart),
    path('Person_10/sum/',       Person_10_sum),

    path('Person_11/add/',       Person_11_add),
    path('Person_11/delete/',    Person_11_delete),
    path('Person_11/addSmart/',  Person_11_addSmart),
    path('Person_11/sum/',       Person_11_sum),

    path('Person_12/add/',       Person_12_add),
    path('Person_12/delete/',    Person_12_delete),
    path('Person_12/addSmart/',  Person_12_addSmart),
    path('Person_12/sum/',       Person_12_sum),

    path('Person_13/add/',       Person_13_add),
    path('Person_13/delete/',    Person_13_delete),
    path('Person_13/addSmart/',  Person_13_addSmart),
    path('Person_13/sum/',       Person_13_sum),

    path('Person_14/add/',       Person_14_add),
    path('Person_14/delete/',    Person_14_delete),
    path('Person_14/addSmart/',  Person_14_addSmart),
    path('Person_14/sum/',       Person_14_sum),

    path('Person_15/add/',       Person_15_add),
    path('Person_15/delete/',    Person_15_delete),
    path('Person_15/addSmart/',  Person_15_addSmart),
    path('Person_15/sum/',       Person_15_sum),
]
