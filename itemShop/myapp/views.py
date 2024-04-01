from django.shortcuts import render




def index(request):
    return render(request, 'index.html')

def first(request):
    return render(request, 'first.html')
