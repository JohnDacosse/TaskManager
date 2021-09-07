from django.contrib import admin
from .models import *

# CRUD de la table Customer via le panneau d'administration
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'profession')
    search_fields = ['name', 'email']
    list_per_page = 25

# CRUD de la table Task via le panneau d'administration
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'location', 'startDate', 'endDate', 'user', 'status')
    search_fields = ('title', 'location')
    list_editable = ('status', )
    list_filter = ('status', 'user')
    autocomplete_fields = ('customer', 'user')
    list_per_page = 25

# CRUD de la table Schedule via le panneau d'administration
# Idée abandonnée | Non implémenté
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'startDate', 'endDate')
    search_fields = ['title']
    filter_horizontal = ('user', )
    list_per_page = 25
