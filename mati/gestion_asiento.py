from conexion_base_de_datos import ConexionGestionEvento

class Asiento(ConexionGestionEvento):
    def __init__(self, nombre_base_de_datos, asiento_id=None, numero=None, ocupado=None, salon_id=None):
        super().__init__(nombre_base_de_datos)
        self.asiento_id = asiento_id
        self.numero = numero
        self.ocupado = ocupado
        self.salon_id = salon_id

    def crear_tabla(self):
        self.cursor.execute('''
        -- Tabla de asientos
        CREATE TABLE IF NOT EXISTS asientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_asiento INTEGER NOT NULL,
            salon_id INTEGER NOT NULL,
            evento_id INTEGER,
            ocupado INTEGER DEFAULT 0, -- 0: Libre, 1: Ocupado
            FOREIGN KEY (salon_id) REFERENCES salones(id) ON DELETE CASCADE,
            FOREIGN KEY (evento_id) REFERENCES eventos(id)
        );
                            ''')
        self.conexion.commit()
        print("Tabla 'asientos' creado con exito.")

    def insertar_muchos(self, consulta, parametros=()):
        self.cursor.executemany(consulta, parametros)
        self.conexion.commit()

asientos = Asiento("Base de datos.db")

asientos.crear_tabla()


asientos.cerrar_conexion()
