from django.contrib import admin
from todo.forms import  TaskForm
from todo.models import Task


class  TaskAdmin(admin.ModelAdmin):
    form = TaskForm

admin.site.register(Task, TaskAdmin)
