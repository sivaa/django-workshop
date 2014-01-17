from django.contrib import admin
from todo.forms import  TaskForm
from todo.models import Task


class  TaskAdmin(admin.ModelAdmin):
    list_filter = ('priority', 'last_date', 'done',)
    list_display = ('name', 'priority', 'last_date', 'done',)
    search_fields = ('name',)

    form = TaskForm

admin.site.register(Task, TaskAdmin)
