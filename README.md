## Proyecto para aprender Urls y Views en Django

- **Path Dinamico:** Consiste en responder solicitudes a urls que no mantengan un valor fijo o estatico
- **Convertidores:** Permite responder segun el tipo de dato que se envie en la url y convertirlo e igualmente recibirlo en el parametro de la vista que se accione.
- **Redirecciones:** Consiste que podamos reenviar la solicitud a otra url de la cual se envio originalmente.
- **HTTP Status Code:** Consiste en enviar un codigo al cliente en la respuesta HTTP, que se usa para indicarle cual fue el estado o resultado de la solicitud que nos envio(200 a 299 respuesta exitosa, 300-399 Redirection, 400-499 Client Error, 500-599, Server Error)
    - HttpResponse: 200 Success/Ok
    - HttpResponseRedirect: 302 Found
    - HttpResponseNotFound: 404 Not Found
- **Named Urls:** Permite dar un nombre a las urls o paths para referenciarlos.
- **Funcion reverse:** Es una funcion que permite construir el path o ruta completa proporcionandole el nombre de la ruta o url de la cual queremos que obtenga su ruta completa, permitiendo que el codigo sea mas dinamico ya que no dependemos de la ruta en duro si no que la genera completa en base al nombre. permitiendo si en un futuro se modifica la ruta principal para acceder a la ruta, este genere la ruta completa sin importar el cambio.