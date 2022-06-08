from django import forms
from .models import TaskModel


class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'deadline', 'priority', 'employers', 'progress']
