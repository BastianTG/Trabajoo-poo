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

    def agregar_asistente(self, nombre,  evento_id, ):
        self.conexion.ejecutar(
            "INSERT INTO asistentes (nombre, asiento_id, ) VALUES (?, ?,)",
            (nombre, evento_id, )
        )
        print(f"Asistente '{nombre}' agregado al evento con ID {evento_id}.")

    def existe_tabla(self,nombre_tabla):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name=?
        ''', (nombre_tabla,))
        if cursor.fetchone():
            return True
        return False

    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
        -- Tabla de asistentes
        CREATE TABLE IF NOT EXISTS asistentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            evento_id INTEGER NOT NULL,
            ticket_id INTEGER,
            asiento_id INTEGER,
            FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
            FOREIGN KEY (ticket_id) REFERENCES tickets(id),
            FOREIGN KEY (asiento_id) REFERENCES asientos(id)
        );
                            ''')
        conexion.commit()
        conexion.close()
        print("Tabla 'asistentes' creado con exito.")
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
def menu_asistente():
    

    conexion = ConexionSQLite3('eventos.db')
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
            # asiento_id = int(input("Ingrese el ID del asiento: "))
            # ticket_id = int(input("Ingrese el ID del ticket: "))
            asistente.agregar_asistente(nombre,  evento_id)
        elif opcion == "3":
            asiento.mostrar_asientos_disponibles()
        elif opcion == "4":
            conexion.cerrar()
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
    
        asistentes= Asistente(conexion)

    # Creación de la tabla asientos.
        if not asistentes.existe_tabla('asistentes'):
            asistentes.crear_tabla()
        else:
            print("La tabla 'asistentes' ya esta creada.")



# Ejecutar el menú principal
menu_asistente()
