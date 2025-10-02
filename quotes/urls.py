# Creamos este archivo para definir el patron de urls o rutas para esta aplicacion
# de forma independiente. permitiendo que sea mas modular la app y podamos desacoplarla e implementarla
# en otro proyecto, ya que tendra sus propias rutas y simplemente añadimos las rutas de la app a las rutas principales.

from django.urls import path
from . import views


# Siempre el patron de urls se define en una variable con este nombre
urlpatterns = [
    path('<day>', views.day_quote)
]
