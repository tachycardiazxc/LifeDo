from django import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.forms import UserCreationForm


class UserCreationView(views.View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        creation_form = UserCreationForm()
        return render(request, template_name='user/registration.html', context={
            'creation_form': creation_form
        })

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        creation_form = UserCreationForm(request.POST)
        if creation_form.is_valid() and creation_form.password_validation():
            creation_form.save()
            cleaned = creation_form.cleaned_data
            # User.objects.create(
            #     username=cleaned.get('username'),
            #     first_name=cleaned.get('first_name'),
            #     last_name=cleaned.get('last_name'),
            #     email=cleaned.get('email'),
            #     password=cleaned.get('password1'),
            #     date_joined=timezone.now(),
            # )
            username = cleaned.get('username')
            raw_password = cleaned.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        return render(request, template_name='user/registration.html', context={
            'creation_form': creation_form
        })


class UserAuthenticationView(views.View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        authentication_form = AuthenticationForm()
        return render(request, template_name='user/login.html', context={
            'authentication_form': authentication_form
        })

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        authentication_form = AuthenticationForm(request.POST)
        if authentication_form.is_valid():
            username = authentication_form.cleaned_data.get('username')
            raw_password = authentication_form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, template_name='user/login.html', context={
            'authentication_form': authentication_form
        })


class UserLogoutView(LogoutView):
    next_page = '/'
