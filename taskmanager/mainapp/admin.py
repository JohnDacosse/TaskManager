from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'profession')
    search_fields = ['name', 'email']


#class UserAdmin(admin.ModelAdmin):
#    list_display = ('username',)
#    search_fields = ['username']


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'location', 'startDate', 'endDate', 'status')
    search_fields = ['title', 'location']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'startDate', 'endDate')
    search_fields = ['title']


#class UserTaskAdmin(admin.ModelAdmin):
#    list_display = ('user', 'task', 'startDate', 'endDate')
#    search_fields = ['user']


class UserScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'schedule')
    search_fields = ['user']


admin.site.register(Clients, ClientAdmin)
#admin.site.register(Users, UserAdmin)
admin.site.register(Tasks, TaskAdmin)
admin.site.register(Schedules, ScheduleAdmin)
# admin.site.register(Status)
#admin.site.register(UserTasks, UserTaskAdmin)
