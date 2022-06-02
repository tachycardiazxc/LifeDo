from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': 'Пароли не совпадают',
    }

    username = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'name ': "name",
                'id': "name",
                'placeholder': "Имя пользователя",
            }
        )
    )
    first_name = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'name ': "name",
                'id': "name",
                'placeholder': "Имя",
            }
        )
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'name ': "name",
                'id': "name",
                'placeholder': "Фамилия",
            }
        )
    )
    email = forms.EmailField(
        min_length=2,
        max_length=128,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type': "text",
                'name ': "name",
                'id': "name",
                'placeholder': "Электронная почта",
            }
        )
    )
    password1 = forms.CharField(
        min_length=8,
        max_length=64,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': "password",
                'name ': "name",
                'id': "name",
                'placeholder': "Пароль",
            }
        )
    )
    password2 = forms.CharField(
        min_length=8,
        max_length=64,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': "password",
                'name ': "name",
                'id': "name",
                'placeholder': "Повторите пароль",
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def password_validation(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class AuthenticationForm(forms.Form):

    username = forms.CharField(
        min_length=2,
        max_length=16,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'name ': "name",
                'id': "name",
                'placeholder': "Имя пользователя",
            }
        )
    )
    password = forms.CharField(
        min_length=8,
        max_length=64,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': "password",
                'name ': "name",
                'id': "name",
                'placeholder': "Пароль",
            }
        )
    )
