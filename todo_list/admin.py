from django.contrib import admin
from .models import List


class ListConf(admin.ModelAdmin):
    list_display = ('id', 'item', 'completed', 'user')
    list_editable = ('completed',)
    

# Register your models here.
admin.site.register(List, ListConf)


