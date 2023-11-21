from django.contrib import admin
from .models import Official

class OfficialAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'role', 'phone', 'pic')

admin.site.register(Official, OfficialAdmin)
