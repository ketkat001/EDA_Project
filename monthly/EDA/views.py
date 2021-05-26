from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'eda/home.html')


def data(request):
    return render(request, 'eda/data.html')


def eda(request):
    return render(request, 'eda/eda.html')