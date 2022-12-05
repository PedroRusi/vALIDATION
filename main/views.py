from django.shortcuts import render, HttpResponse
from .forms import RegisterForm, LoginForm
# Create your views here.

def index(request):
    form = RegisterForm()
    return render(request, 'index.html', {'form': form})

def site(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            pswd = request.POST.get('password')
            return render(request, 'site.html', {'name': name, 'pswd': pswd, 'email': email})

def Login(request):
    form = LoginForm()
    return render(request, 'Login.html', {'form': form})


def user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pswd = request.POST.get('password')
        if name == 'User1' and pswd == '12345678':
            return render(request, 'user.html', {'name': name})
        else:
            return HttpResponse('Вы не зарегистрированы.<br> Не хотите зарегистрироваться?<br><a href="/">Registration</a>')


