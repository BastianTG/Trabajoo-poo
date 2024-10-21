from conexion_base_de_datos import *
from gestion_salon import *

class Evento(ConexionGestionEvento):
    def __init__(self, nombre_bd, evento_id, nombre, fecha, hora_inicio, hora_termino, salon_id):
        super().__init__(nombre_bd)
        self.evento_id = evento_id
        self.nombre = nombre
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_termino = hora_termino
        self.salon_id = salon_id

    # Método para verificar si la tabla existe
    def existe_tabla(self,nombre_tabla):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name=?
        ''', (nombre_tabla,))
        if cursor.fetchone():
            return True
        return False
    
    # Método heredado que crea la tabla eventos.
    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
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
                            ''')
        conexion.commit()
        conexion.close()
        print("Tabla 'eventos' creada con exito")

    def registrar_asientos(self, evento_id, salon_id, capacidad):
        
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT MAX(id) FROM eventos")
        evento_id = cursor.fetchone()[0]
        # Crear asientos y tickets basados en la capacidad del salón
        for i in range(1, capacidad + 1):
            # Insertar asientos con evento_id
            cursor.execute(
                "INSERT INTO asientos (numero_asiento, salon_id, ocupado, evento_id) VALUES (?, ?, ?, ?) ",
                (i, salon_id, 0, evento_id)  # Aquí se incluye evento_id
            )
            # No necesitas obtener el último ID aquí, ya que se puede manejar directamente con el evento_id
            
            
        conexion.commit()
        conexion.close()

    def insertar(self, nombre_evento, fecha, hora_inicio, hora_termino, salon_id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO eventos (nombre, fecha, hora_inicio, hora_termino, salon_id) VALUES (?, ?, ?, ?, ?)""",
            (nombre_evento, fecha, hora_inicio, hora_termino, salon_id))
        conexion.commit()
        conexion.close()
    
    def eliminar(self, evento_id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            DELETE FROM eventos WHERE id = ? """, (evento_id,))
        conexion.commit()
        conexion.close()
        
def agregar_evento(evento):

    print("Salones disponibles: ")
    for salon in salon_1.leer():
        print(f"{salon[0]}: {salon[1]} (Capacidad: {salon[2]})")

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
    # evento_id = input("")

    
    # Obtener el ID del evento recién creado
    evento_id = evento.obtener_ultimo_id()
        # Insertar el evento en la base de datos
    evento.insertar(nombre_evento, fecha, hora_inicio, hora_termino, salon_id)
    # Obtener la capacidad del salón seleccionado
    capacidad = next(s[2] for s in salon_1.leer() if s[0] == salon_id)
    
    # Registrar automáticamente los asientos 
    evento.registrar_asientos(evento_id, salon_id, capacidad)

    print("Evento, asientos y tickets agregados con éxito")

def eliminar_evento(evento):
    
    id_evento = int(input("Seleccione un evento para eliminar por su ID: "))
    evento.eliminar(id_evento)
    print("Evento eliminado con exito")

def menu_evento(evento):
    bandera = True

    while bandera:
        print("\tBienvenido al menu de gestion de eventos")
        print("\nIngrese la opcion que desee: ")
        print("\t1.- Agregar Evento")
        print("\t2.- Eliminar Evento")
        print("\tIngrese Q para salir.")

        eleccion_usuario = input("> ")

        if eleccion_usuario == "1":
            agregar_evento(evento)
            #time.sleep(1)
        elif eleccion_usuario == "2":
            eliminar_evento(evento)
        elif eleccion_usuario == "q" or eleccion_usuario == "Q":
            print("salir\n")
            #time.sleep(1)
            print("Saliendo del programa\n")
            bandera = False
        else:
            print("El valor ingresado es incorrecto")
            print("Volviendo al menu principal\n")
            #time.sleep(1)

nombre_bd = "eventos.db"

evento = Evento(nombre_bd, None, None, None, None, None, None)

evento.crear_tabla()


