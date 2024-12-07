def ingresar_notas_criterio():
    while True:
        try:
            nota_eximicion = float(input("  Nota de eximición (entre 1 y 7): "))
            nota_aprobacion = float(input("  Nota de aprobación (entre 1 y 7): "))
            if 1 <= nota_eximicion <= 7 and 1 <= nota_aprobacion <= 7:
                return [nota_eximicion, nota_aprobacion]
            else:
                print("  Ambas notas deben estar entre 1 y 7. Intenta nuevamente.")
        except ValueError:
            print("  Por favor, introduce números válidos.")

def ingresar_porcentajes():
    while True:
        porcentajes = []
        suma = 0
        for i in range(4):
            while True:
                try:
                    porcentaje = float(input(f"  Porcentaje de la nota {i + 1} (en %): "))
                    if 0 <= porcentaje <= 100:
                        porcentajes.append(porcentaje)
                        suma += porcentaje
                        break
                    else:
                        print("  El porcentaje debe estar entre 0 y 100.")
                except ValueError:
                    print("  Por favor, introduce un número válido.")
        if suma == 100:
            return porcentajes
        else:
            print(f"  La suma de los porcentajes es {suma}. Deben sumar exactamente 100%. Inténtalo de nuevo.")

def ingresar_notas():
    notas = []
    for i in range(4):
        while True:
            entrada = input(f"  Ingresa la nota {i + 1} (o escribe 'no' para dejarla vacía): ").strip().lower()
            if entrada == "no":
                notas.append(None)
                break
            try:
                nota = float(entrada)
                if 1 <= nota <= 7:
                    notas.append(nota)
                    break
                else:
                    print("  La nota debe estar entre 1 y 7.")
            except ValueError:
                print("  Por favor, introduce un número válido o 'no'.")
    return notas

def agregar_asignatura(matriz_criterios, matriz_porcentajes, matriz_notas, nombres_asignaturas):
    nombre = input("\nIntroduce el nombre de la nueva asignatura: ").strip()
    nombres_asignaturas.append(nombre)
    print(f"\nConfigurando la asignatura '{nombre}':")
    criterios = ingresar_notas_criterio()
    porcentajes = ingresar_porcentajes()
    notas = ingresar_notas()
    matriz_criterios.append(criterios)
    matriz_porcentajes.append(porcentajes)
    matriz_notas.append(notas)
    print(f"Asignaura '{nombre}' agregada exitosamente.")

def cambiar_porcentajes(matriz_porcentajes, nombres_asignaturas):
    print("\nAsignaturas disponibles:")
    for i, nombre in enumerate(nombres_asignaturas, start=1):
        print(f"  {i}. {nombre}: {matriz_porcentajes[i - 1]}")

    while True:
        try:
            seleccion = int(input("\nSelecciona una asignatura por su número (o escribe 0 para cancelar): "))
            if seleccion == 0:
                break
            if 1 <= seleccion <= len(matriz_porcentajes):
                print(f"\nCambiando porcentajes para la asignatura '{nombres_asignaturas[seleccion - 1]}':")
                matriz_porcentajes[seleccion - 1] = ingresar_porcentajes()
                print("Porcentajes actualizados.")
                break
            else:
                print("  Selección inválida. Intenta nuevamente.")
        except ValueError:
            print("  Por favor, introduce un número válido.")

def completar_notas(matriz_notas, nombres_asignaturas):
    print("\nAsignaturas disponibles:")
    for i, nombre in enumerate(nombres_asignaturas, start=1):
        print(f"  {i}. {nombre}: {matriz_notas[i - 1]}")

    while True:
        try:
            seleccion = int(input("\nSelecciona una asignatura por su número (o escribe 0 para cancelar): "))
            if seleccion == 0:
                break
            if 1 <= seleccion <= len(matriz_notas):
                asignatura = matriz_notas[seleccion - 1]
                print(f"\nAsignatura seleccionada: {nombres_asignaturas[seleccion - 1]}")
                for i, nota in enumerate(asignatura):
                    if nota is None:
                        while True:
                            entrada = input(f"  Ingresa una nota para el espacio {i + 1} (entre 1 y 7): ").strip()
                            try:
                                nueva_nota = float(entrada)
                                if 1 <= nueva_nota <= 7:
                                    asignatura[i] = nueva_nota
                                    break
                                else:
                                    print("  La nota debe estar entre 1 y 7.")
                            except ValueError:
                                print("  Por favor, introduce un número válido.")
                print(f"\nNotas actualizadas: {asignatura}")
                break
            else:
                print("  Selección inválida. Intenta nuevamente.")
        except ValueError:
            print("  Por favor, introduce un número válido.")

def mostrar_matrices(matriz_criterios, matriz_notas, matriz_porcentajes, nombres_asignaturas):
    print("\nMatriz de Criterios, Notas y Porcentajes:")
    for i, (criterios, notas, porcentajes, nombre) in enumerate(zip(matriz_criterios, matriz_notas, matriz_porcentajes, nombres_asignaturas)):
        print(f"Asignatura {i + 1} - {nombre}:")
        print(f"  Nota de Eximición: {criterios[0]}, Nota de Aprobación: {criterios[1]}")
        for j in range(4):
            print(f"    Nota {j + 1}: {notas[j]}, Porcentaje: {porcentajes[j]}%")

def main():
    matriz_criterios = []
    matriz_porcentajes = []
    matriz_notas = []
    nombres_asignaturas = []

    while True:
        print("\nMenú principal:")
        print("  1. Configurar todo desde cero.")
        print("  2. Agregar una nueva asignatura.")
        print("  3. Cambiar porcentajes de notas.")
        print("  4. Agregar notas a una asignatura.")
        print("  5. Mostrar matrices.")
        print("  0. Salir.")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            matriz_criterios.clear()
            matriz_porcentajes.clear()
            matriz_notas.clear()
            nombres_asignaturas.clear()
            try:
                num_asignaturas = int(input("\nIntroduce el número de asignaturas: "))
                if num_asignaturas <= 0:
                    print("El número de asignaturas debe ser mayor que cero.")
                    continue
                for _ in range(num_asignaturas):
                    agregar_asignatura(matriz_criterios, matriz_porcentajes, matriz_notas, nombres_asignaturas)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "2":
            agregar_asignatura(matriz_criterios, matriz_porcentajes, matriz_notas, nombres_asignaturas)
        elif opcion == "3":
            cambiar_porcentajes(matriz_porcentajes, nombres_asignaturas)
        elif opcion == "4":
            completar_notas(matriz_notas, nombres_asignaturas)
        elif opcion == "5":
            mostrar_matrices(matriz_criterios, matriz_notas, matriz_porcentajes, nombres_asignaturas)
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
