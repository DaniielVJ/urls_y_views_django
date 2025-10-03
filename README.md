## Proyecto para aprender Urls y Views en Django
- UwU


- **Path Dinamico:** Consiste en responder solicitudes a urls que no mantengan un valor fijo o estatico
- **Convertidores:** Permite responder segun el tipo de dato que se envie en la url y convertirlo e igualmente recibirlo en el parametro de la vista que se accione.
- **Redirecciones:** Consiste que podamos reenviar la solicitud a otra url de la cual se envio originalmente.
- **HTTP Status Code:** Consiste en enviar un codigo al cliente en la respuesta HTTP, que se usa para indicarle cual fue el estado o resultado de la solicitud que nos envio(200 a 299 respuesta exitosa, 300-399 Redirection, 400-499 Client Error, 500-599, Server Error)
    - HttpResponse: 200 Success/Ok
    - HttpResponseRedirect: 302 Found
    - HttpResponseNotFound: 404 Not Found