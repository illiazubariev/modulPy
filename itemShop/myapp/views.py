from django.shortcuts import render
from django.http import HttpResponse




def any(request):
    return HttpResponse('any texts')

def index(request):
    my_num = 33
    my_str = 'some string'
    return render(request, 'index.html', {
        'my_num': my_num, 'my_str': my_str
        })