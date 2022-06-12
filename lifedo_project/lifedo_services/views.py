from django import views
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm


class TaskView(views.View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        user = User.objects.get(username=request.user)
        tasks = TaskModel.objects.filter(employers=user)
        each_task_form = []
        for task in tasks:
            each_task_form.append(TaskForm(instance=task))
        return render(request, template_name='task/task.html', context={
            'tasks_form': each_task_form
        })
