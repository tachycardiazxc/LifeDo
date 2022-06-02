from django.shortcuts import render
from django import views


class IndexView(views.View):

    def get(self, request):
        return render(request, template_name='index.html', context={

        })
