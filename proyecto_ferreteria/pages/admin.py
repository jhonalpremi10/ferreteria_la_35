# pages/admin.py
from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')  # Mostrar en la lista de administración
    search_fields = ('title', 'content')      # Campos de búsqueda

admin.site.register(Page, PageAdmin)


