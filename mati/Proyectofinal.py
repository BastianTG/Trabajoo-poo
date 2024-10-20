import sqlite3
import time

class ConexionSQLite3:                                                              #Clase con la que conectar la aplicacion a una base de datos sqlite3
    def __init__(self, nombre_base_datos):                                          #Codigo correspondiente a la conexion de la base de datos
        self.nombre_base_datos = nombre_base_datos
        self.conexion = sqlite3.connect(nombre_base_datos)
        self.cursor = self.conexion.cursor()

    def verificar_ticket(self, ticket_id):                                          # Metodo que verifica si el ticket ingresado existe y ya ha sido asignado a un asistente.
        self.cursor.execute("SELECT * FROM asistentes WHERE ticket_id = ?", (ticket_id,))  #Ejecute el comando para buscar en la base de datos el codigo del ticket que se desea verificar
        asistente = self.cursor.fetchone()                                          # Aplicar método fetchone que devuelve una fila de la base de datos
        if asistente:
            return True, "El ticket es válido y está asignado a un asistente."      #Mensaje que se envie si el codigo se encuentra registrado en la tabla asistentes
        else:
            return False, "El ticket no es válido o no está asignado."              #mensaje si el codigo no se encuentra en la tabla asistentes

    def cerrar_conexion(self):                                                      #Metodo para cerrar la base de datos
        self.conexion.close()



    def menu_principal():                                                          # Funcion que lleva al menu prinipal
    bandera = True
    conexion_sqlite = ConexionSQLite3("Base de datos")                             #Conexion a la base de del centro de eventos

    while bandera:                                                                 #Texto que se muestra al principio del programa
        print("\tBienvenido a la cosita de eventos")
        print("\nQué acción desea hacer ahora?")
        print("\t1.- OPCIONES DE EVENTO")
        print("\t2.- OPCIONES DE ASISTENTE")
        print("\t3.- VALIDAR TICKET")
        print("\tIngrese Q para salir.\n")

        eleccion_usuario = input("> ")                                             #Varible que guarda la opcion ingresada por el usuario

        if eleccion_usuario == "1":                                                #Confirmacion de que los valores ingresados son validos
            print("coso 1\n")

        elif eleccion_usuario == "2":
            print("coso 2\n")

        elif eleccion_usuario == "3":                                              #Lo que se realiza si el usuario selecciona la opcion 3 "Validar ticket"
            cod_a_validar = input("Ingrese el código del ticket a validar: ").strip() # Se le pide al usuario ingresar el codigo a validar,  se guarda en la variable cod_a_validar y se le quitan los espacios
            if cod_a_validar.isdigit():                                                     # Validar que el código del ticket es un número
                es_valido, mensaje = conexion_sqlite.verificar_ticket(int(cod_a_validar))   #si es valido se utliza el metodo verificar_ticket
                print(mensaje)                                                              # Mostrar el mensaje resutado de la verificación del ticket
            else:
                print("El código del ticket debe ser un número válido.")            #mensaje en caso del que codigo no sea valido

        elif eleccion_usuario == "q" or eleccion_usuario == "Q":
            print("salir\n")
            time.sleep(1)
            print("Saliendo del programa\n")
            bandera = False

        else:                                                                      #Mensaje en caso de que no ingrese un valor valido y se vuelve al menu principal 
            print("El valor ingresado es incorrecto")
            print("Volviendo al menu principal\n")
            time.sleep(1)



                
if __name__ == "__main__":
    menu_principal()
    
                
