from django.contrib import admin
from .models import TaskModel


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'priority', 'progress']
    list_filter = ['priority', 'progress']
