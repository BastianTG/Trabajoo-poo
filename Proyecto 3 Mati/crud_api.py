import requests
import json
from autenticacion import Autenticacion

class APIClient:
    """ 
    Clase que gestiona el CRUD de la API seleccionada.
    """
    def __init__(self, base_url, api_key):
        self.base_url = base_url # Atributo que contiene la URL de la API.
        self.api_key = api_key # Atributo que contiene la API key correspondiente.

    """ Metodo que realiza la captura de datos de la API. """
    def get_data(self, endpoint):
        print("\n--- Ver albums ---")
        url = f"{self.base_url}/{endpoint}" # URL de la API con el endpoint correspondiente a lo que queremos ver.
        #print(f"Consultando: {url}")
        headers = {"Authorization": f"Bearer {self.api_key}"} # Variable que contiene la api key, aunque no es necesaria para procesar las solicitudes.
        response = requests.get(url, headers=headers)

        if response.status_code == 200:  # Verifica si el servidor mando una respuesta exitosa o no.
            data = response.json()
            #print(data)

            while True: # Ciclo que pregunta el numero de elementos que el usuario quiere ver.
                try:
                    # Pregunta el numero de elementos que quiere ver en pantalla.
                    num_datos = int(input("Ingrese el número de datos que desea ver: "))
                    if num_datos > 0 and num_datos <= len(data): # Condición que el numero de elementos sea positivo y menor o igual que el total de datos.
                        break
                    else: 
                        print("Por favor, ingrese un número mayor que 0 y menor a la cantidad total de elementos.")
                        # Print que sale cuando el usuario ingresa un numero negativo o mayor a la cantidad de elementos.
                except ValueError: 
                    print("Entrada inválida. Ingrese un número entero.") 
                    # Print que sale cuando el usuario un dato que no es entero.

            print("Datos obtenidos con GET:")
            # Mostramos los elementos que quiera el usuario
            print(json.dumps(data[:num_datos], indent=4))
            return data # Retorna el objeto data para quuien lo haya invocado. Permite la reutilización de datos. 
        else:
            print(f"Error al obtener datos:", response.status_code) # Acusa cualquier error al procesar los datos.
            return None # sin comentarios...
    
    """ Metodo que crea un nuevo album en la API. """
    def post_data(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}" # URL de la API seleccionada para postear algo.
        headers = {"Authorization": f"Bearer {self.api_key}"} # Variable que contiene la api key, aunque no es necesaria para procesar las solicitudes.
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201: # Verifica si el servidor mando una respuesta exitosa o no.
            print("Datos enviados con POST:")
            # Mostramos los elementos que queremoos que tenga el nuevo album en la API.
            print(json.dumps(response.json(), indent=4))
            return response.json() # Retorna los elementos que enviamos con POST,
        else:
            print("Error al enviar los datos a la API:", response.status_code) # Acusa cualquier error al procesar los datos.
            #print(response.text)
            return None # sin comentarios...

    def put_data(self, endpoint, data, item_id):
        url = f"{self.base_url}/{endpoint}/{item_id}" # URL de la API para el elemento a actualizar.
        headers = {"Authorization": f"Bearer {self.api_key}"} # Variable que contiene la api key, aunque no es necesaria para procesar las solicitudes.
        response = requests.put(url, json=data, headers=headers)

        if response.status_code == 200: # Verifica si el servidor mando una respuesta exitosa o no.
            print("Datos actualizados con PUT: ")
            # Mostramos los datos actualizados de la API.
            print(json.dumps(response.json(), indent=4))
            return response.json() # Retorna los elementos que enviamos con PUT.
        else:
            print("Error al actualizar los datos:", response.status_code) # Acusa cualquier error al procesar los datos.
            print(response.text)
            return None # sin comentarios...
            

    def delete_data(self, endpoint, item_id):
        url = f"{self.base_url}/{endpoint}/{item_id}" # URL de la API para el elemento a eliminar.
        headers = {"Authorization": f"Bearer {self.api_key}"} # Variable que contiene la api key, aunque no es necesaria para procesar las solicitudes..
        response = requests.delete(url, headers=headers)

        if response.status_code == 200: # Verifica si el servidor mando una respuesta exitosa o no.
            data = response.json()
            print("Datos eliminados con DELETE:")
            print(f"Album con ID {item_id} ha sido eliminado con exito.")
            return True
        else:
            print("Error al eliminar datos:", response.status_code) # Acusa cualquier error al procesar los datos.
            #print(response.text)
            return None # sin comentarios...

def solicitar_datos_album(): # Metodo que solicita al usuario los datos necesarios para crear un nuevo album.
    print("\n--- Crear un nuevo album ---")
    title = input("Ingrese el título del álbum: ")
    while True:
        try: # Verifica que el ID ingresado sea numerico y positivo.
            user_id = int(input("Ingrese el ID del usuario: "))
            if user_id > 0:
                break
            else: # Ingreso de un numero negativo.
                print("Ingrese un numero positivo, por favor.")
        except ValueError: # Ingreso de algo que no es un numero.
            print("Por favor, ingrese un número entero para el ID.")
    
    nuevo_post = { # Se crea un diccionario con los datos ingresados por el usuario.
            "title": title,
            "userId": user_id                
        }
    # Retorna todos los datos ingresados por el usuario en su nuevo formato.
    return nuevo_post

def solicitar_actualizar(item_id): # Metodo que solicita al usuario los datos necesarios para actualizar un elemento.
    print("\n--- Actualizar un album ---")
    title = input("Ingrese el título del álbum: ")
    while True:
        try: # Verifica que el ID ingresado sea numerico y positivo.
            user_id = int(input("Ingrese el ID del usuario: "))
            if user_id > 0:
                break
            else: # Ingreso de un numero negativo.
                print("Ingrese un numero positivo, por favor.")
        except ValueError: # Ingreso de algo que no es un numero.
            print("Por favor, ingrese un número entero para el ID.")
    
    nueva_actualizacion = { # Se crea un diccionario con los datos ingresados por el usuario.
                "userId": user_id,
                "id": item_id,
                "title": title
            }
    # Retorna todos los datos ingresados por el usuario en su nuevo formato.
    return nueva_actualizacion

def menu():
    endpoint_api = "albums"
    api_url = "https://jsonplaceholder.typicode.com"
    api_key = Autenticacion.obtener_api_key()
    client = APIClient(api_url, api_key)

    while True:
        print("\n--- Menú de Opciones de la API ---")
        print("1. Ver albums")
        print("2. Crear un nuevo album")
        print("3. Actualizar un album")
        print("4. Borrar album")
        print("5. Salir")

        opcion = input("Seleccione una opción (1, 2, 3, 4 o 5): ")

        if opcion == "1": # Opcion que usa el metodo GET.
            client.get_data(endpoint_api) # Usando el endpoint se hace uso del metodo GET.
        elif opcion == "2": # Opcion que usa el metodo POST.
            nuevo_album = solicitar_datos_album() # Se pide al usuario los datos para realizar el POST.
            client.post_data(endpoint_api, nuevo_album) # Usando el endpoint se hace uso del metodo POST.
        elif opcion == "3": # Opcion que usar el metodo PUT.
            while True:
                try:
                    id_actualizar = int(input("Ingrese el ID del álbum a actualizar: "))
                    if id_actualizar > 0 and id_actualizar <= 100: # Verifica si el id a actualizar se encuentra dentro de los limites del elemento.
                        break
                    else:
                        print("Ingrese un ID dentro del rango permitido.") # Se ingreso un número fuera del rango.
                except ValueError:
                    print("Por favor, ingrese un número entero.") # Se ingreso algo que no es entero.
            nuevo_album = solicitar_actualizar(id_actualizar)
            client.put_data(endpoint_api, nuevo_album, id_actualizar)
        elif opcion == "4": # Opcion que usa el metodo DELETE.
            while True:
                try:
                    id_eliminar = int(input("Ingrese el ID del álbum a eliminar: "))
                    if id_eliminar > 0 and id_eliminar <= 100: # Verifica si el id a actualizar se encuentra dentro de los limites del elemento.
                        break
                    else:
                        print("Ingrese un ID dentro del rango permitido.") # Se ingreso un número fuera del rango.
                except ValueError:
                    print("Por favor, ingrese un número entero.") # Se ingreso algo que no es entero.
            client.delete_data(endpoint_api, id_eliminar)
        elif opcion == "5": # Opcion que sale del menu de la API.
            print("Saliendo del menú de la API.") 
            break 
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()