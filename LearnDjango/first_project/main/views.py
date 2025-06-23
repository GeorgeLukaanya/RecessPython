from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def login_views(request):
    return render(request, 'login.html')

def signup_views(request):
    return render(request, 'signup.html')

def detect_views(request):
    return render(request, 'detect.html')

def about_views(request):
    return render(request, 'about.html')