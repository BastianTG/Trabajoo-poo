from conexion_base_de_datos import ConexionGestionEvento


# Clase que gestiona los salones iniciales.
class Salon(ConexionGestionEvento):
    def __init__(self, nombre_base_de_datos, salon_id=None, nombre=None, capacidad=None):
        super().__init__(nombre_base_de_datos)
        self.salon_id = salon_id
        self.nombre = nombre
        self.capacidad = capacidad

    # Función para verificar si la tabla existe
    def existe_tabla(self,nombre_tabla):
        self.cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND name=?
        ''', (nombre_tabla,))
        if self.cursor.fetchone():
            return True
        return False

    def crear_tabla(self):
            self.cursor.execute('''
            -- Tabla de salones
            CREATE TABLE IF NOT EXISTS salones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                capacidad INTEGER NOT NULL
            );
                            ''')
            self.conexion.commit()
            print("Tabla 'salones' creada con exito.")

# Creación del objeto Salon para crear tabla e insertar valores por defecto.
salones = Salon("eventos.db")

# Creación de la tabla salones.
if not salones.existe_tabla('salones'):
    salones.crear_tabla()

    # Creación de los salones por defecto.
    salones.insertar("INSERT INTO salones (id, nombre, capacidad) VALUES (?, ?, ?)",
                 (1, "Salon Principal", 25))
    salones.insertar("INSERT INTO salones (id, nombre, capacidad) VALUES (?, ?, ?)",
                 (2, "Teatro", 16))
    salones.insertar("INSERT INTO salones (id, nombre, capacidad) VALUES (?, ?, ?)",
                 (3, "Comedor", 16))
    print("Salones insertados con exito.")

    # Cerrar la conexión despues de los cambios realizados.
    salones.cerrar_conexion()
else:
    print("La tabla 'salones' ya esta creada")






    
        