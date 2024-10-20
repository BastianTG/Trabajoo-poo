import sqlite3

# Clase que hace la conexion a la base de datos con las operaciones crud.
class ConexionGestionEvento:
    def __init__(self, nombre_base_de_datos="Base de datos.db"):
        # Conexion a la base de datos, si no existe la crea
        self.nombre_base_de_datos = nombre_base_de_datos
        self.conexion = sqlite3.connect(nombre_base_de_datos)
        self.cursor = self.conexion.cursor()
    
    # Función para crear las tablas necesarias.
    def crear_tabla(self):
        pass

    # Función para insertar datos.    
    def insertar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.conexion.commit()

    # Función para leer datos.    
    def leer(self, consulta):
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        for fila in resultados:
            print(fila)
            
    # Función para obtener el ultimo id.    
    def obtener_ultimo_id(self):
        return self.cursor.lastrowid
    
    # Función para actualizar datos.
    def actualizar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.conexion.commit()
    
    # Función para eliminar datos.
    def eliminar(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.conexion.commit()
    
    # Función para cerrar la conexión con la base de datos.
    def cerrar_conexion(self):
        self.conexion.close()
        print("Conexion cerrada.")

