from django.contrib import admin

from To_Do_app.models import ToDo

# Register your models here.

class TaskDisplay(admin.ModelAdmin):
    list_display = ('task', 'done','created_at','updated_at')

admin.site.register(ToDo, TaskDisplay)