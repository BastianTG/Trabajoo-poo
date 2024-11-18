from Autentificacion import *
from Crud_API import *
from Crud_BD import *


def menu_principal():

    while True:
        print("\n--- Menú de Opciones para la Base de Datos ---")
        print("1. CRUD API")
        print("2. CRUD Base de Datos")
        print("3. Sincronizar Registro")
        print("4. Salir")

        opcion = input("Seleccione una opción (1, 2, 3, 4 o 5): ")

        if opcion == "1":
            menu_API()
        elif opcion == "2":
            menu_BD()
        elif opcion == "3":
            db_client = DatabaseClient()
            endpoint_api = "albums"
            api_url = "https://jsonplaceholder.typicode.com"
            api_key = Autenticacion.obtener_api_key()
            client = APIClient(api_url, api_key)
            values=client.get_data_ID_Values(endpoint_api)
            print(values)
            db_client.insertar_datos_ID(values[2],values[0],values[1])
        elif opcion == "4":
            print("Saliendo del menú de la base de datos.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()