import sqlite3

# Clase para conectarse a la base de datos
class ConexionSQLite3:
    def __init__(self, nombre_base_datos):
        self.conexion = sqlite3.connect(nombre_base_datos)
        self.cursor = self.conexion.cursor()

    def ejecutar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.conexion.commit()
        return self.cursor

    def leer(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def cerrar(self):
        self.conexion.close()

# Clase para seleccionar eventos
class Evento:
    def __init__(self, conexion):
        self.conexion = conexion

    def seleccionar_eventos(self):
        eventos = self.conexion.leer("SELECT id, nombre FROM eventos")
        print("Eventos disponibles:")
        for evento in eventos:
            print(f"ID: {evento[0]}, Nombre: {evento[1]}")
        return eventos

# Clase para agregar asistentes
class Asistente:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar_asistente(self, nombre, evento_id):
        self.conexion.ejecutar(
            "INSERT INTO asistentes (nombre, evento_id) VALUES (?, ?)",
            (nombre, evento_id)
        )
        print(f"Asistente '{nombre}' agregado al evento con ID {evento_id}.")

# Clase para mostrar asientos disponibles
class Asiento:
    def __init__(self, conexion):
        self.conexion = conexion

    def mostrar_asientos_disponibles(self):
        asientos = self.conexion.leer("SELECT numero FROM asientos WHERE ocupado = 0")
        print("Asientos disponibles:")
        for asiento in asientos:
            print(f"Asiento número: {asiento[0]}")
        return asientos

# Menú principal para interactuar con las clases
def menu_principal():
    conexion = ConexionSQLite3('Base de datos.db')
    evento = Evento(conexion)
    asistente = Asistente(conexion)
    asiento = Asiento(conexion)

    while True:
        print("\n--- Menú de Gestión ---")
        print("1. Seleccionar evento")
        print("2. Agregar asistente")
        print("3. Mostrar asientos disponibles")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            evento.seleccionar_eventos()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del asistente: ")
            evento_id = int(input("Ingrese el ID del evento: "))
            asistente.agregar_asistente(nombre, evento_id)
        elif opcion == "3":
            asiento.mostrar_asientos_disponibles()
        elif opcion == "4":
            conexion.cerrar()
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú principal
menu_principal()
