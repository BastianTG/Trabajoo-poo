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
            ocupado INTEGER DEFAULT 0, -- 0: Libre, 1: Ocupado
            FOREIGN KEY (salon_id) REFERENCES salones(id) ON DELETE CASCADE
        );
                            ''')
        self.conexion.commit()
        print("Tabla 'asientos' creado con exito.")

    def insertar_muchos(self, consulta, parametros=()):
        self.cursor.executemany(consulta, parametros)
        self.conexion.commit()

asientos = Asiento("Base de datos.db")

asientos.crear_tabla()

asientos_por_defecto = [
        (1, 1, 0, 1), (2, 2, 0, 1), (3, 3, 0, 1), (4, 4, 0, 1),
        (5, 5, 0, 1), (6, 6, 0, 1), (7, 7, 0, 1), (8, 8, 0, 1),
        (9, 9, 0, 1), (10, 10, 0, 1), (11, 11, 0, 1), (12, 12, 0, 1),
        (13, 13, 0, 1), (14, 14, 0, 1), (15, 15, 0, 1), (16, 16, 0, 1),
        (17, 17, 0, 1), (18, 18, 0, 1), (19, 19, 0, 1), (20, 20, 0, 1),
        (21, 21, 0, 1), (22, 22, 0, 1), (23, 23, 0, 1), (24, 24, 0, 1),
        (25, 25, 0, 1), (26, 1, 0, 2), (27, 2, 0, 2), (28, 3, 0, 2),
        (29, 4, 0, 2), (30, 5, 0, 2), (31, 6, 0, 2), (32, 7, 0, 2),
        (33, 8, 0, 2), (34, 9, 0, 2), (35, 10, 0, 2), (36, 11, 0, 2),
        (37, 12, 0, 2), (38, 13, 0, 2), (39, 14, 0, 2), (40, 15, 0, 2),
        (41, 16, 0, 2), (42, 1, 0, 3), (43, 2, 0, 3), (44, 3, 0, 3),
        (45, 4, 0, 3), (46, 5, 0, 3), (47, 6, 0, 3), (48, 7, 0, 3),
        (49, 8, 0, 3), (50, 9, 0, 3), (51, 10, 0, 3), (52, 11, 0, 3),
        (53, 12, 0, 3), (54, 13, 0, 3), (55, 14, 0, 3), (56, 15, 0, 3),
        (57, 16, 0, 3)
    ]

asientos.insertar_muchos("INSERT INTO asientos (id, numero_asiento, ocupado, salon_id) VALUES (?, ?, ?, ?)",
                         (asientos_por_defecto))

print("Asientos insertados correctamente")

asientos.cerrar_conexion()