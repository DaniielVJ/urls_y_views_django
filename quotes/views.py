from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Si el dia que el usuario envia coincide con alguna clave del diccionario
# devolveremos la palabra asociada a esa clave o dia
days_of_week={
    'monday': 'Pienso, Luego existo',
    'tuesday': 'La vida es un sueño',
    'wednesday': 'El conocimiento es poder',
    'thursday': 'Sé el cambio que quieras ver',
    'friday': 'Solo se que no se nada',
    'saturday': 'Vive como si fuera el ultimo dia',
    'sunday': 'Da un poquito mas todos los dias'
}



# si el day se manda como integer se acciona esta vista
def days_week_with_number(request, day):
    return HttpResponse(day)


# Si el dia se manda como texto acciona esta vista
def days_week(request, day):
    # Mi version de logica
    if day not in days_of_week:
        return HttpResponseNotFound('No hay frase para ese dia')
    return HttpResponse(days_of_week[day])
   

    # Version del profe
    try:
        quote_text=days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("No hay frase para ese dia")
    