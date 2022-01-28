from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User     #비밀번호 검증, 로그인처리
from django.contrib import auth, messages
from .forms import RegisterForm, LoginForm, ApplicationForm
from .models import Application
from django.db.models import ObjectDoesNotExist   #db에서 어떤 데이터가 없으면 exception 발생

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def search(request):
    context = {}
    return render(request, 'pages/search.html', context)

def more(request):
    context = {}
    return render(request, 'pages/more.html', context)

def mylibrary__playlist(request):
    context = {}
    return render(request, 'pages/mylibrary__playlist.html', context)

def bookmark(request):
    context = {}
    return render(request, 'pages/bookmark.html', context)

def mylibrary__book(request):
    context = {}
    return render(request, 'pages/mylibrary__book.html', context)

def mylibrary__people(request):
    context = {}
    return render(request, 'pages/mylibrary__people.html', context)

def ashlee_vance_book(request):
    context = {}
    return render(request, 'pages/ashlee_vance_book.html', context)

def ashlee_vance_book_ch1(request):
    context = {}
    return render(request, 'pages/ashlee_vance_book_ch1.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(email, email, password)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'pages/register.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=email, password=password)  #규칙이 맞으면 user에 none이 아닌 객체가 들어감
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.warning(request, '계정 혹은 비밀번호를 확인해주세요.')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'pages/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def update_application(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user

            try:
                original = Application.objects.get(user=request.user)
                application.id = original.id
            except ObjectDoesNotExist:
                pass
            finally:
                application.save()

            return HttpResponseRedirect('/application/update/')

    else:
        try:
            original = Application.objects.get(user=request.user)
            form = ApplicationForm(instance=original)
            cancelable = True
        except ObjectDoesNotExist:
            form = ApplicationForm()
            cancelable = False

    context = {
        'form': form,
        'cancelable': cancelable
    }
    return render(request, 'pages/update_application.html', context)