from conexion_base_de_datos import *
from gestion_salon import *

class Evento(ConexionGestionEvento):
    def __init__(self, nombre_base_de_datos, evento_id=None, nombre=None, fecha=None, hora_inicio=None, hora_termino=None, salon_id=None):
        super().__init__(nombre_base_de_datos)
        self.evento_id = evento_id
        self.nombre = nombre
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_termino = hora_termino
        self.salon_id = salon_id

    def crear_tabla(self):
        self.cursor.executescript('''
        -- Tabla de eventos
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fecha DATE NOT NULL,
            hora_inicio TIME NOT NULL,
            hora_termino TIME NOT NULL,
            salon_id INTEGER NOT NULL,
            FOREIGN KEY (salon_id) REFERENCES salones(id) ON DELETE CASCADE
        );
        -- Tabla de asientos
        CREATE TABLE IF NOT EXISTS asientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_asiento INTEGER NOT NULL,
            salon_id INTEGER NOT NULL,
            evento_id INTEGER NOT NULL,
            ocupado INTEGER DEFAULT 0, -- 0: Libre, 1: Ocupado
            FOREIGN KEY (salon_id) REFERENCES salones(id) ON DELETE CASCADE,
            FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE
        );
        -- Tabla de tickets
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento_id INTEGER NOT NULL,
            asiento_id INTEGER NOT NULL,
            asignado INTEGER DEFAULT 0, -- 0: No asignado, 1: Asignado
            FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
            FOREIGN KEY (asiento_id) REFERENCES asientos(id) ON DELETE CASCADE
        );
        ''')
        self.conexion.commit()

    def registrar_asientos_y_tickets(self, evento_id, salon_id, capacidad):
        # Crear asientos y tickets basados en la capacidad del salón
        for i in range(1, capacidad + 1):
            # Insertar asientos
            self.cursor.execute(
                "INSERT INTO asientos (numero_asiento, salon_id, evento_id, ocupado) VALUES (?, ?, ?, ?)",
                (i, salon_id, evento_id, 0)
            )
            asiento_id = self.obtener_ultimo_id()
            # Insertar ticket asociado
            self.cursor.execute(
                "INSERT INTO tickets (evento_id, asiento_id, asignado) VALUES (?, ?, ?)",
                (evento_id, asiento_id, 0)
            )
        self.conexion.commit()

def agregar_evento():
    salon = Salon("Base de datos.db")
    evento = Evento("Base de datos.db")
    
    # Mostrar lista de salones disponibles
    print("Salones disponibles:")
    salones = salon.obtener_salones()
    for s in salones:
        print(f"ID: {s[0]}, Nombre: {s[1]}, Capacidad: {s[2]}")
    
    # Solicitar datos del usuario
    salon_id = int(input("Seleccione un salón por su ID: "))
    fecha = input("Ingrese una fecha (DD/MM/AAAA): ")
    # Convertir fecha al formato 'YYYY-MM-DD'
    try:
        dia, mes, año = fecha.split('/')
        fecha = f"{año}-{mes.zfill(2)}-{dia.zfill(2)}"
    except ValueError:
        print("Formato de fecha incorrecto. Use DD/MM/AAAA.")
        return

    hora_inicio = input("Ingrese la hora de inicio (HH:MM:SS): ")
    hora_termino = input("Ingrese la hora de termino (HH:MM:SS): ")

    nombre_evento = input("Nombre del evento: ")

    # Insertar el evento en la base de datos
    evento.insertar(
        "INSERT INTO eventos (nombre, fecha, hora_inicio, hora_termino, salon_id) VALUES (?, ?, ?, ?, ?)",
        (nombre_evento, fecha, hora_inicio, hora_termino, salon_id)
    )
    
    # Obtener el ID del evento recién creado
    evento_id = evento.obtener_ultimo_id()
    # Obtener la capacidad del salón seleccionado
    capacidad = next(s[2] for s in salones if s[0] == salon_id)
    
    # Registrar automáticamente los asientos y tickets
    evento.registrar_asientos_y_tickets(evento_id, salon_id, capacidad)

    print("Evento, asientos y tickets agregados con éxito")

# Ejecución del menú principal
if __name__ == "__main__":
    evento = Evento("Base de datos.db")
    evento.crear_tabla()
    menu_evento()
    evento.cerrar_conexion()

