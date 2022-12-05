from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=255, label="Введите имя", widget=forms.TextInput(attrs={"class": "name", 'placeholder': 'Name'}))

    email = forms.EmailField(label="Введите ваш Email", widget=forms.EmailInput(attrs={"class": "email", 'placeholder': 'Email'}))
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput(attrs={"class": "pswd", 'placeholder': 'Password'}))

class LoginForm(forms.Form):
    name = forms.CharField(max_length=255, label="Введите имя", widget=forms.TextInput(attrs={"class": "name", 'placeholder': 'Name'}))
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput(attrs={"class": "pswd", 'placeholder': 'Password'}))