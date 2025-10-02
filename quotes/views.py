from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def days_week_with_number(request, day):
    return HttpResponse(day)


# Responde a una url dinamica de tipo string
def days_week(request, day):
    quote_text = None
    if day == 'monday':
        quote_text = 'Pienso, Luego existo'
    elif day == 'tuesday':
        quote_text = 'La vida es un sueño'
    else:
        return HttpResponseNotFound('<h1>No se encuentra esa cita</h1>')

    return HttpResponse(quote_text)