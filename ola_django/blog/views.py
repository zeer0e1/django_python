# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog(request):
    print(request)
    print('Ala o usuário fazendo cagada')
    return HttpResponse('Home do blog')
