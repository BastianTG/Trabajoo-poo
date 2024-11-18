class Autenticacion:
    """ Clase que verifica una autenticación correcta para conectarse a la API. """

    def obtener_api_key():
        """ Retorna la api key del usuario, luego de verificar si es correcta o no. """

        while True: # Bucle para verificar si la clave ingresada es correcta
            eleccion = input("Ingrese su clave API asignada: ")
            if eleccion.capitalize() == "Prueba":
                eleccion = "$2a$10$aWspDhHqE2rOYCl8lk69C.pKa9p6mXlrqy3rKtQXghyELXhPqN74e"
                #print(eleccion)
                return eleccion # Retorna la clave correcta para usarla en el programa.
            else:
                # Clave ingresada incorrecta, se pregunta nuevamente.
                print("Clave incorrecta, ingrese nuevamente.")