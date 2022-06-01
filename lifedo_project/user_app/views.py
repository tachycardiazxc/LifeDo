from django import views
from django.shortcuts import render


class IndexView(views.View):

    def get(self, request):
        return render(request, template_name='index.html', context={

        })
