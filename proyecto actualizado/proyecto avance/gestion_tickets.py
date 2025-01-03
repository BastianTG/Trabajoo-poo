from conexion_base_de_datos import *

class Ticket(ConexionGestionEvento):
    def __init__(self, nombre_bd, ticket_id, evento_id, asiento_id, asignado):
        super().__init__(nombre_bd)
        self.ticket_id = ticket_id
        self.evento_id = evento_id
        self.asiento_id = asiento_id
        self.asignado = asignado

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
        -- Tabla de tickets
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                evento_id INTEGER,
                asiento_id INTEGER,
                FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
                FOREIGN KEY (asiento_id) REFERENCES asientos(id) ON DELETE CASCADE
            );
        ''')
        conexion.commit()
        conexion.close()
        print("Tabla 'tickets' creada con exito")           

nombre_bd = "eventos.db"

ticket = Ticket(nombre_bd, None, None, None, None)

ticket.crear_tabla()