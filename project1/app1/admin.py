from django.contrib import admin
from . models import Data

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ['order_date','region','manager','salesman','items','units']
admin.site.register(Data, DataAdmin)


