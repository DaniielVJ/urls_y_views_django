from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def day_quote(request, day):
    quote_text = None
    if day == 'monday':
        quote_text = 'Es Lunes'
    elif day == 'tuesday':
        quote_text = 'Es Martes'
    else:
        return HttpResponseNotFound('<h1>No se encuentra esa cita</h1>')

    return HttpResponse(quote_text)