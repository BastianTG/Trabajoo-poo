import sqlite3

class DatabaseClient:
    """
    Clase que gestiona el CRUD de la base de datos SQLite3.
    """
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)  # Conecta a la base de datos
        self.create_table() # Se crea la tabla apenas se inicia la clase. 

    def create_table(self):
        """ Crea la tabla 'albums' si no existe. """

        self.connection.execute("""
                CREATE TABLE IF NOT EXISTS albums (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    userId INTEGER NOT NULL
                )
        """)

    def leer_datos(self):
        """ Obtiene todos los registros de la tabla. """

        consulta = self.connection.execute("SELECT * FROM albums").fetchall() # Consulta SQL que entrega todos los elementos encontrados en la tabla albums.
        if consulta: # Verifica si la consulta devuelve datos o si es vacia.
            print("\n--- Registros en la base de datos ---")
            for i in consulta:
                print(f"ID: {i[0]}, Title: {i[1]}, UserID: {i[2]}")
                self.connection.commit() # Guarda las consultas realizadas.
        else: # Mensaje que devuelve si la consulta es vacia.
            print("No hay registros en la base de datos.")

    def insertar_datos_ID(self, titulo, user_id, id):
        """ Inserta un nuevo registro en la tabla. """

        consulta = "INSERT INTO albums (title, userId, id) VALUES (? , ?, ?)"
        self.connection.execute(consulta, [titulo, user_id, id])
        print(f"Registro insertado con éxtio")
        self.connection.commit()

    def insertar_datos(self, titulo, user_id):
        """ Inserta un nuevo registro en la tabla. """

        consulta = "INSERT INTO albums (title, userId) VALUES (? , ?)"
        self.connection.execute(consulta, [titulo, user_id])
        print(f"Registro insertado con éxtio")
        self.connection.commit()

    def actualizar_datos(self, titulo, user_id, id):
        """ Actualiza un registro existente por su ID. """

        consulta = "UPDATE albums SET title = ?, userId = ? WHERE id = ?"
        self.connection.execute(consulta, [titulo, user_id, id])
        print("Registro actualizado con exito.")
        self.connection.commit()

    def eliminar_datos(self, id_eliminar):
        """ Elimina un registro de la tabla por su ID. """

        consulta = "DELETE FROM albums WHERE id = ?"
        self.connection.execute(consulta, [id_eliminar])
        print(f"Registro con el ID {id_eliminar} eliminado con exito.")
        self.connection.commit()

def menu_BD():
    db_client = DatabaseClient()

    while True:
        print("\n--- Menú de Opciones para la Base de Datos ---")
        print("1. Ver registros")
        print("2. Crear un nuevo registro")
        print("3. Actualizar un registro")
        print("4. Eliminar un registro")
        print("5. Salir")

        opcion = input("Seleccione una opción (1, 2, 3, 4 o 5): ")

        if opcion == "1":
            db_client.leer_datos()
        elif opcion == "2":
            print("\n--- Crear un nuevo registro de album ---")
            titulo = input("Ingresa el titulo del nuevo album: ")
            while True:
                try: # Verifica que el ID ingresado sea numerico y positivo.
                    user_id = int(input("Ingrese el ID del usuario: "))
                    if user_id > 0:
                        break
                    else: # Ingreso un numero negativo.
                        print("Ingrese un numero positivo, por favor.")
                except ValueError: # Ingreso de algo que no es un numero.
                    print("Por favor, ingrese un número entero para el ID.")
            db_client.insertar_datos(titulo, user_id)
        elif opcion == "3":
            print("\n--- Actualizar un registro ---")
            while True:
                try:
                    id_actualizar = int(input("Ingrese el ID del álbum a actualizar: "))
                    if id_actualizar > 0: # Verifica si el id a actualizar se encuentra dentro de los limites del elemento.
                        break
                    else:
                        print("Ingrese un ID dentro del rango permitido.") # Se ingreso un número fuera del rango.
                except ValueError:
                    print("Por favor, ingrese un número entero.") # Se ingreso algo que no es entero.
            while True:
                try: # Verifica que el ID del Usuario a actualizar sea numerico y positivo.
                    user_id = int(input("Ingrese el ID del usuario: "))
                    if user_id > 0:
                        break
                    else: # Ingreso de un numero negativo.
                        print("Ingrese un numero positivo, por favor.")
                except ValueError: # Ingreso de algo que no es un numero.
                    print("Por favor, ingrese un número entero para el ID.")           
            titulo = input("Ingrese el nuevo titulo del registro: ")
            db_client.actualizar_datos(titulo, user_id, id_actualizar)
        elif opcion == "4":
            while True:
                try:
                    id_eliminar = int(input("Ingrese el ID del álbum a eliminar: "))
                    if id_eliminar > 0: # Verifica si el id a actualizar se encuentra dentro de los limites del elemento.
                        break
                    else:
                        print("Ingrese un ID dentro del rango permitido.") # Se ingreso un número fuera del rango.
                except ValueError:
                    print("Por favor, ingrese un número entero.") # Se ingreso algo que no es entero.
            db_client.eliminar_datos(id_eliminar)
        elif opcion == "5":
            print("Saliendo del menú de la base de datos.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_BD()