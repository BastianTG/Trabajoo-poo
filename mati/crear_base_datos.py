import sqlite3

def crear_base_datos():
    # Conexión a la base de datos (si no existe, se crea automáticamente)
    conexion = sqlite3.connect('Base de datos.db')
    cursor = conexion.cursor()

    # Crear las tablas
    cursor.executescript('''
        -- Tabla de salones
        CREATE TABLE IF NOT EXISTS salones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            capacidad INTEGER NOT NULL
        );

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

        -- Tabla de asientos
        CREATE TABLE IF NOT EXISTS asientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_asiento INTEGER NOT NULL,
            salon_id INTEGER NOT NULL,
            ocupado INTEGER DEFAULT 0, -- 0: Libre, 1: Ocupado
            FOREIGN KEY (salon_id) REFERENCES salones(id) ON DELETE CASCADE
        );

        -- Tabla de tickets
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento_id INTEGER NOT NULL,
            asistente_id INTEGER NOT NULL,
            asiento_id INTEGER NOT NULL,
            FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
            FOREIGN KEY (asistente_id) REFERENCES asistentes(id),
            FOREIGN KEY (asiento_id) REFERENCES asientos(id)
        );
    ''')

    # Insertar los datos iniciales de los salones
    cursor.executescript('''
        INSERT INTO salones (id, nombre, capacidad) VALUES (1, 'Salón Principal', 25);
        INSERT INTO salones (id, nombre, capacidad) VALUES (2, 'Teatro', 16);
        INSERT INTO salones (id, nombre, capacidad) VALUES (3, 'Comedor', 16);
    ''')

    # Insertar los datos de los asientos
    asientos = [
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

    cursor.executemany('''
        INSERT INTO asientos (id, numero_asiento, ocupado, salon_id)
        VALUES (?, ?, ?, ?);
    ''', asientos)

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()
    print("Base de datos y asientos creados con éxito.")

if __name__ == "__main__":
    crear_base_datos()