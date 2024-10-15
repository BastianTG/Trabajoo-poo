import time

def menu_principal():
    bandera = True

    while bandera:
        print("\tBienvenido a la cosita de eventos")
        print("\nQué acción desea hacer ahora?")
        print("\t1.- Opciones de Evento")
        print("\t2.- Cosa 2")
        print("\t3.- Cosa 3")
        print("\tIngrese Q para salir.\n")

        eleccion_usuario = input("> ")

        if eleccion_usuario == "1":
            print("Entrando al menú de eventos\n")
            time.sleep(1)
            
        elif eleccion_usuario == "2":
            print("coso 2\n")
        elif eleccion_usuario == "3":
            print("coso 3\n")
        elif eleccion_usuario == "q" or eleccion_usuario == "Q":
            print("salir\n")
            time.sleep(1)
            print("Saliendo del programa\n")
            bandera = False
        else:
            print("El valor ingresado es incorrecto")
            print("Volviendo al menu principal\n")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()