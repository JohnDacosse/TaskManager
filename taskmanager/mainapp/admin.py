from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'profession')
    search_fields = ['name', 'email']
    list_per_page = 25


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'location', 'startDate', 'endDate', 'user', 'status')
    search_fields = ('title', 'location')
    list_editable = ('status', )
    list_filter = ('status', 'user')
    autocomplete_fields = ('customer', 'user')
    list_per_page = 25


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'startDate', 'endDate')
    search_fields = ['title']
    filter_horizontal = ('user', )
    list_per_page = 25
