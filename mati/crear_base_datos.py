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
            evento_id INTEGER NOT NULL,
            ocupado INTEGER DEFAULT 0, -- 0: Libre, 1: Ocupado
            FOREIGN KEY (salon_id) REFERENCES salones(id) ON DELETE CASCADE
            FOREIGN KEY (evento_id) REFERENCES eventos(id)
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
