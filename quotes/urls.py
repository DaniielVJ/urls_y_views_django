# Creamos este archivo para definir el patron de urls o rutas para esta aplicacion
# de forma independiente. permitiendo que sea mas modular la app y podamos desacoplarla e implementarla
# en otro proyecto, ya que tendra sus propias rutas y simplemente añadimos las rutas de la app a las rutas principales.

from django.urls import path
from . import views


# Siempre el patron de urls se define en una variable con este nombre
urlpatterns = [
    path('<int:day>', views.days_week_with_number), # path que responde si se envia un numero
    path('<str:day>', views.days_week, name='day-quote') # este responde si se envia un texto
]



# PATH DINAMICO: se especifica con <parametro>, esto permite que el usuario ingrese cualquier ruta en la url y nuestra web
# va accionar una vista aunque no exista ese path, y el valor de ese path se pasa a un parametro de la vista con el mismo nombre.

# Convertidores de Rutas: Permite especificar segun el tipo de dato que se envie en la url, ejecutar una logica u otra
# int:url para indicar que si se envia un numero, str:url para indicar que se envia un string, por defecto si no se especifica
# django toma todo como string

# Keyword name en los path, permite dar un nombre a la url y identificar con este.