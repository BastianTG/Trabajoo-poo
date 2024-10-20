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
        self.cursor.execute('''
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
        
def agregar_evento():
    salon = Salon("Base de datos.db")
    evento = Evento("Base de datos.db")
    
    salon_id = int(input("Seleccione un salon por su ID: "))

    fecha = input("Ingrese una fecha (DD/MM/AA): ")

    hora_inicio = input("Ingrese la hora de inicio (HH:MM:SS): ")
    hora_termino = input("Ingrese la hora de termino (HH:MM:SS): ")

    nombre_evento = input("Nombre del evento: ")
    evento.insertar("INSERT INTO eventos (id, nombre, fecha, hora_inicio, hora_termino, salon_id) VALUES (?, ?, ?, ?, ?, ?)",
                    (1,nombre_evento, fecha, hora_inicio, hora_termino, salon_id))
    print("Evento agregado con exito")

def eliminar_evento():
    evento = Evento("Base de datos.db")

    id_evento = int(input("Seleccione un evento para eliminar por su ID: "))
    evento.eliminar("DELETE FROM eventos WHERE id = ?",(id_evento)) 
    print("Evento eliminado con exito")

def menu_evento():
    bandera = True

    while bandera:
        print("\tBienvenido al menu de gestion de eventos")
        print("\nIngrese la opcion que desee: ")
        print("\t1.- Agregar Evento")
        print("\t2.- Eliminar Evento")
        print("\tIngrese Q para salir.")

        eleccion_usuario = input("> ")

        if eleccion_usuario == "1":
            agregar_evento()
            #time.sleep(1)
        elif eleccion_usuario == "2":
            eliminar_evento()
        elif eleccion_usuario == "q" or eleccion_usuario == "Q":
            print("salir\n")
            #time.sleep(1)
            print("Saliendo del programa\n")
            bandera = False
        else:
            print("El valor ingresado es incorrecto")
            print("Volviendo al menu principal\n")
            #time.sleep(1)   

evento = Evento("Base de datos.db")

evento.crear_tabla()

menu_evento()

evento.cerrar_conexion()
