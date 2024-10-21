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


# Clase para manejar eventos
class Evento:
    def __init__(self, conexion):
        self.conexion = conexion

    def seleccionar_eventos(self):
        eventos = self.conexion.leer("SELECT id, nombre FROM eventos")
        print("Eventos disponibles:")
        for evento in eventos:
            print(f"ID: {evento[0]}, Nombre: {evento[1]}")
        return eventos


# Clase para manejar asistentes
class Asistente:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_asiento_disponible(self):
        asiento = self.conexion.leer("SELECT id FROM asientos WHERE ocupado = 0 LIMIT 1")
        return asiento[0][0] if asiento else None

    def generar_ticket(self, evento_id, asiento_id, asistente_id):
        self.conexion.ejecutar(
            "INSERT INTO tickets (evento_id, asiento_id) VALUES (?, ?)",
            (evento_id, asiento_id)
        )
        print(f"Ticket generado para el asistente {asistente_id} con asiento {asiento_id} en el evento {evento_id}.")

    def agregar_asistente(self, nombre, evento_id):
        # 1. Agregar el asistente a la tabla asistentes
        self.conexion.ejecutar(
            "INSERT INTO asistentes (nombre, evento_id) VALUES (?, ?)",
            (nombre, evento_id)
        )
        asistente_id = self.conexion.cursor.lastrowid  # Obtener el id del asistente recién insertado
        print(f"Asistente '{nombre}' agregado con ID {asistente_id} al evento con ID {evento_id}.")

        # 2. Asignar automáticamente un asiento disponible
        asiento_id = self.obtener_asiento_disponible()
        if asiento_id:
            # Cambiar estado del asiento a ocupado
            self.conexion.ejecutar("UPDATE asientos SET ocupado = 1 WHERE id = ?", (asiento_id,))
            print(f"Asiento {asiento_id} asignado y marcado como ocupado.")
            
            # 3. Generar ticket para el asistente
            self.generar_ticket(evento_id, asiento_id, asistente_id)
        else:
            print("No se pudo asignar un asiento porque no hay disponibles.")

    def existe_tabla(self, nombre_tabla):
        resultado = self.conexion.leer("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (nombre_tabla,))
        return len(resultado) > 0

    def crear_tabla_asistentes(self):
        self.conexion.ejecutar('''
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
        print("Tabla 'asistentes' creada con éxito.")


# Clase para mostrar asientos disponibles
class Asiento:
    def __init__(self, conexion):
        self.conexion = conexion

    def mostrar_asientos_disponibles(self):
        asientos = self.conexion.leer("SELECT numero_asiento FROM asientos WHERE ocupado = 0")
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

    # Crear la tabla de asistentes si no existe
    if not asistente.existe_tabla('asistentes'):
        asistente.crear_tabla_asistentes()
    else:
        print("La tabla 'asistentes' ya está creada.")

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
menu_asistente()
