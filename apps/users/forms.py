from django import forms


from apps.users.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логин"
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )