from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from cerberus import Validator
from decimal import Decimal, InvalidOperation
import numpy as np
import matplotlib.pyplot as plt

# Variables globales (matrices a utilizar).
matriz_criterios = []
matriz_porcentajes = []
matriz_notas = []
nombres_asignaturas = []

# Funcion que valida el formato al ingresar una nueva asignatura.
def validacion_asignatura(esquema_asignatura_dado):

    # Esquema de validación de los datos de una asignatura.
    esquema_asignatura = {
        "nombre": {"type": "string", "minlength": 1, "empty": False},
        "eximir": {"type": "float", "min": 1, "max": 7},
        "aprobar": {"type": "float", "min": 1, "max": 7},
        "porcentajes": {
            "type": "list",
            "schema": {"type": "float", "min": 0, "max": 100},
            "minlength": 4,
            "maxlength": 4
        }
    }

    # Variable que define el esquema a comparar.
    asignatura_valida = Validator(esquema_asignatura)

    # Preguntas que verifican si el esquema y los datos ingresados son iguales.
    if asignatura_valida.validate(esquema_asignatura_dado):
        print("Datos válidos.")
    else:
        print("Datos invalidos")
        print(asignatura_valida.errors)

# Función que transforma todo número a decimal para facilitar los cálculos.
def decimal(valor, campo):
    try:
        return Decimal(valor)
    except InvalidOperation:
        raise ValueError(f"{campo} debe ser un número válido.")

# Función para agregar las asignaturas que quiera el usuario.
def agregar_asignatura():
    # Función que guarda en las listas o matrices los datos ingresados por el usuario.
    def guardar_asignatura():
        try:
            nombre = entry_nombre.get().strip()
            eximir = decimal(entry_eximir.get(), "Nota de eximición")
            aprobar = decimal(entry_aprobar.get(), "Nota de aprobación")
            porcentajes = [
                decimal(entry_porcentaje_1.get(), "Porcentaje 1"),
                decimal(entry_porcentaje_2.get(), "Porcentaje 2"),
                decimal(entry_porcentaje_3.get(), "Porcentaje 3"),
                decimal(entry_porcentaje_4.get(), "Porcentaje 4")
            ]

            # Validar los rangos de las notas para aprobar y eximirse, además de la suma de los porcentajes.
            if not (4 <= eximir <= 7 and aprobar == 4):
                raise ValueError("Las notas de eximición (mayor/igual a 4 y menor/igual a 7) y/o aprobación (mayor a 4) han sido ingresadas incorrectamente.")
            if sum(porcentajes) != 100:
                raise ValueError(f"La suma de los porcentajes debe ser exactamente 100, suma: {sum(porcentajes)}")
            
            # Comparar los datos ingresados con el esquema definido.
            datos = {
                "nombre" : nombre,
                "eximir" : float(eximir),
                "aprobar" : float(aprobar),
                "porcentajes" : [float(p) for p in porcentajes]
            }

            validacion_asignatura(datos)

            # Guardar datos válidos en sus respectivas listas o matrices.
            nombres_asignaturas.append(nombre)
            matriz_criterios.append([eximir, aprobar])
            matriz_porcentajes.append([p for p in porcentajes])

            messagebox.showinfo("Éxito", f"Asignatura {nombre} agregada y validada con éxito.")
            ventana_agregar.destroy()

            #print(nombres_asignaturas)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
       
    # Creación de la ventana para agregar asignaturas.
    ventana_agregar = Toplevel()
    ventana_agregar.title("Agregar asignatura")
    ventana_agregar.geometry("400x300")

    label_nombre = Label(ventana_agregar, text="Nombre de la asignatura")
    label_nombre.pack()

    entry_nombre = Entry(ventana_agregar)
    entry_nombre.config(justify="left")
    entry_nombre.pack()

    label_aprobar = Label(ventana_agregar, text="Nota de aprobación")
    label_aprobar.pack()

    entry_aprobar = Entry(ventana_agregar)
    entry_aprobar.config(justify="left")
    entry_aprobar.pack()

    label_eximir = Label(ventana_agregar, text="Nota de eximición (si no corresponde, ingrese nota de aprobación)")
    label_eximir.pack()

    entry_eximir = Entry(ventana_agregar)
    entry_eximir.config(justify="left")
    entry_eximir.pack()

    label_porcentaje = Label(ventana_agregar, text="Porcentajes de evaluación (deben sumar 100)")
    label_porcentaje.pack()

    entry_porcentaje_1 = Entry(ventana_agregar)
    entry_porcentaje_1.config(justify="left")
    entry_porcentaje_2 = Entry(ventana_agregar)
    entry_porcentaje_2.config(justify="left")
    entry_porcentaje_3 = Entry(ventana_agregar)
    entry_porcentaje_3.config(justify="left")
    entry_porcentaje_4 = Entry(ventana_agregar)
    entry_porcentaje_4.config(justify="left")
    entry_porcentaje_1.pack()
    entry_porcentaje_2.pack()
    entry_porcentaje_3.pack()
    entry_porcentaje_4.pack()

    boton_guardar = Button(ventana_agregar, text="Guardar asignatura", command=guardar_asignatura)
    boton_guardar.pack(side="bottom")

# Función para mostrar las asignaturas agregadas por el usuario.
def mostrar_asignaturas():
    if not nombres_asignaturas:
        messagebox.showinfo("Información", "No hay asignaturas registradas.")
        return

    ventana_mostrar = Toplevel()
    ventana_mostrar.title("Asignaturas")
    ventana_mostrar.geometry("400x400")

    #print(nombres_asignaturas)
    
    # Inserta un treeview en la ventana con los nombres de las asignaturas ingresadas.
    vista_arbol = ttk.Treeview(ventana_mostrar, columns=("#", "Asignatura"), show="headings")
    vista_arbol.heading("#", text="Nº")
    vista_arbol.heading("Asignatura", text="Nombre de la Asignatura")
    vista_arbol.pack(fill="both", expand=True)

    for i, nombre in enumerate(nombres_asignaturas, start=1):
        vista_arbol.insert("", "end", values=(i, nombre))

# Función que calcula la ponderación de las distintas asignaturas según las notas que se ingresen.
def calcular_ponderacion():
        
    # Funcion que sirve para ingresar las notas y calcular el promedio según la opción seleccionada.
    def calcular_promedio():
        #print(matriz_criterios)
        numero_asignatura = lista.current()

        # Agregamos lo necesario para ingresar las notas.
        label_nota_1 = Label(ventana_calculo, text="Nota 1")
        label_nota_1.grid(row=6, column=1)

        label_nota_2 = Label(ventana_calculo, text="Nota 2")
        label_nota_2.grid(row=7, column=1)

        label_nota_3 = Label(ventana_calculo, text="Nota 3")
        label_nota_3.grid(row=8, column=1)

        label_nota_4 = Label(ventana_calculo, text="Nota 4")
        label_nota_4.grid(row=9, column=1)

        entry_nota_1 = Entry(ventana_calculo)
        entry_nota_1.grid(row=6, column=2)
        entry_nota_1.config(justify="left")

        label_porcentaje_1 = Label(ventana_calculo, text=f"  {matriz_porcentajes[numero_asignatura][0]} %")
        label_porcentaje_1.grid(row=6, column=3)

        entry_nota_2 = Entry(ventana_calculo)
        entry_nota_2.grid(row=7, column=2)
        entry_nota_2.config(justify="left")

        label_porcentaje_2 = Label(ventana_calculo, text=f"  {matriz_porcentajes[numero_asignatura][1]} %")
        label_porcentaje_2.grid(row=7, column=3)

        entry_nota_3 = Entry(ventana_calculo)
        entry_nota_3.grid(row=8, column=2)
        entry_nota_3.config(justify="left")

        label_porcentaje_3 = Label(ventana_calculo, text=f"  {matriz_porcentajes[numero_asignatura][2]} %")
        label_porcentaje_3.grid(row=8, column=3)

        entry_nota_4 = Entry(ventana_calculo)
        entry_nota_4.grid(row=9, column=2)
        entry_nota_4.config(justify="left")

        label_porcentaje_4 = Label(ventana_calculo, text=f"  {matriz_porcentajes[numero_asignatura][3]} %")
        label_porcentaje_4.grid(row=9, column=3)

        # Función que se encarga de sumar las ponderaciones y entregar el promedio de todas las notas.
        def ponderar():
            nota_1 = entry_nota_1.get()
            nota_2 = entry_nota_2.get()
            nota_3 = entry_nota_3.get()
            nota_4 = entry_nota_4.get()

            if not nota_1.strip(): # Verifica si esta vacío
                nota_1 = "0"
            
            if not nota_2.strip():
                nota_2 = "0"

            if not nota_3.strip():
                nota_3 = "0"
            
            if not nota_4.strip():
                nota_4 = "0"

            matriz_notas.append([Decimal(nota_1), Decimal(nota_2), Decimal(nota_3), Decimal(nota_4)])
            
            # Cálculo de las ponderaciones de las distintas notas.
            ponderacion_1 = Decimal(nota_1) * (matriz_porcentajes[numero_asignatura][0] / 100)
            ponderacion_2 = Decimal(nota_2) * (matriz_porcentajes[numero_asignatura][1] / 100)
            ponderacion_3 = Decimal(nota_3) * (matriz_porcentajes[numero_asignatura][2] / 100)
            ponderacion_4 = Decimal(nota_4) * (matriz_porcentajes[numero_asignatura][3] / 100)

            # print(ponderacion_1)
            # print(ponderacion_2)
            # print(ponderacion_3)
            # print(ponderacion_4)
            # print(matriz_criterios[numero_asignatura])
            # print(matriz_criterios[numero_asignatura][0])
            # print(matriz_criterios[numero_asignatura][1])

            # Cálculo del promedio final.
            promedio_final = ponderacion_1 + ponderacion_2 + ponderacion_3 + ponderacion_4

            # print(promedio_final)

            label_mostrar.configure(text=promedio_final)

            # Mensajes personalizados según el promedio dado, si apruebas o no.
            if promedio_final < matriz_criterios[numero_asignatura][1]:
                label_mensaje.configure(text=f"Has reprobado {nombres_asignaturas[numero_asignatura]}, suerte a la próxima.")
            elif matriz_criterios[numero_asignatura][1] <= promedio_final < matriz_criterios[numero_asignatura][0]:
                label_mensaje.configure(text=f"No te has eximido en {nombres_asignaturas[numero_asignatura]}, tendrás que dar examen.")
                
                # Se agrega las funcionalidades en caso de dar examen.
                label_examen.configure(text="Examen")
                entry_examen.grid(row=14, column=2)
                entry_examen.config(justify="left")
                label_porcentaje_examen.configure(text="  25%")
                boton_examen.grid(row=15, column=2)

                def examen():
                    nota_examen = entry_examen.get()

                    if not nota_examen.strip():
                        nota_examen = "0"

                    ponderacion_examen = float(nota_examen) * (25 / 100)
                    promedio_examen = float(promedio_final) * (75 / 100)
                    ponderacion_final = promedio_examen + ponderacion_examen

                    if ponderacion_final < matriz_criterios[numero_asignatura][1]:
                        label_mensaje_examen.configure(text=f"Has reprobado {nombres_asignaturas[numero_asignatura]} con un {round(ponderacion_final, 1)}, suerte a la próxima.")
                    elif ponderacion_final > matriz_criterios[numero_asignatura][1]:
                        label_mensaje_examen.configure(text=f"Has aprobado {nombres_asignaturas[numero_asignatura]} con un {round(ponderacion_final, 1)}, felicitaciones.")

                boton_examen.grid(row=15, column=2)
                boton_examen.configure(command=examen)

            elif matriz_criterios[numero_asignatura][1] < promedio_final > matriz_criterios[numero_asignatura][0]:
                label_mensaje.configure(text=f"Has aprobado y te has eximido de {nombres_asignaturas[numero_asignatura]} con un {round(promedio_final, 1)}, felicitaciones.")
            elif matriz_criterios[numero_asignatura][1] <= round(promedio_final) and matriz_criterios[numero_asignatura][0] == matriz_criterios[numero_asignatura][1]:
                label_mensaje.configure(text=f"Has aprobado {nombres_asignaturas[numero_asignatura]} con un {round(promedio_final, 1)}, felicitaciones.")

        boton_calcular = Button(ventana_calculo, text="Calcular", command=ponderar)
        boton_calcular.grid(row=10, column=1)

        # Función que reinicia los campos de las notas y el resultado obtenido.
        def reiniciar():
            entry_nota_1.delete(0, END)
            entry_nota_2.delete(0, END)
            entry_nota_3.delete(0, END)
            entry_nota_4.delete(0, END)
            label_mostrar.configure(text="")
            label_mensaje.configure(text="")
            label_examen.configure(text="")
            entry_examen.delete(0, END)
            entry_examen.grid_forget()
            label_porcentaje_examen.configure(text="")
            boton_examen.grid_forget()
            label_mensaje_examen.configure(text="")

        boton_reiniciar = Button(ventana_calculo, text="Reiniciar", command=reiniciar)
        boton_reiniciar.grid(row=10, column=3)

        label_resultado = Label(ventana_calculo, text="Resultado")
        label_resultado.grid(row=11, column=2)

        label_mostrar = Label(ventana_calculo)
        label_mostrar.grid(row=12, column=2)

        label_mensaje = Label(ventana_calculo)
        label_mensaje.grid(row=13, column=2)

        label_examen = Label(ventana_calculo)
        label_examen.grid(row=14, column=1)

        entry_examen = Entry(ventana_calculo)
        entry_examen.grid_forget()

        label_porcentaje_examen = Label(ventana_calculo)
        label_porcentaje_examen.grid(row=14, column=3)

        boton_examen = Button(ventana_calculo, text="Calcular con examen")
        boton_examen.grid_forget()

        label_mensaje_examen = Label(ventana_calculo)
        label_mensaje_examen.grid(row=16, column=2)

        
    if not nombres_asignaturas:
        messagebox.showinfo("Información", "No hay asignaturas registradas.")
        return

    # Creación de la ventana para calcular las distintas ponderaciones.
    ventana_calculo = Toplevel()
    ventana_calculo.title("Resultado de las ponderaciones")
    ventana_calculo.geometry("700x500")

    # Creación de un combobox con los nombres de las distintas asignaturas.
    lista = ttk.Combobox(ventana_calculo, state='readonly', width=20)
    lista.grid(row=0, column=0)
    lista['values'] = nombres_asignaturas

    # Boton que abre la opción para ingresar las notas y calcular las ponderaciones.
    boton_ingresar = Button(ventana_calculo, text="Ingresar notas", command=calcular_promedio)
    boton_ingresar.grid(row=0, column=2)

   # Opción predeterminada del combobox.
    lista.set(nombres_asignaturas[0])

def mostrar_graficos():
    # Validar si existen datos para la creación del gráfico.
    if not nombres_asignaturas or not matriz_notas:
        messagebox.showinfo("Información", "No hay datos para crear un gráfico.")
    
    promedios_graficar = [
        np.nanmean([nota for nota in notas if nota is not None])
        for notas in matriz_notas
    ]

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(nombres_asignaturas, promedios_graficar, color="skyblue")
    plt.title("Promedio de Notas por Asignatura", fontsize=14)
    plt.ylabel("Promedio", fontsize=12)
    plt.xlabel("Asignaturas", fontsize=12)
    plt.ylim(0, 7)  # Limitar rango de promedios a 0-7
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Mostrar gráfico
    plt.show()
        
# Función principal del programa.
def main():
    # Definición de la ventana principal.
    ventana_principal = Tk()
    ventana_principal.title("Promedio Seguro")
    ventana_principal.geometry("600x100")


    boton_agregar = Button(ventana_principal, text="Agregar asignatura", command=agregar_asignatura)
    boton_mostrar = Button(ventana_principal, text="Mostrar Asignaturas", command=mostrar_asignaturas)
    boton_calcular = Button(ventana_principal,text="Calcular ponderación", command=calcular_ponderacion)
    boton_grafico = Button(ventana_principal, text="Mostrar gráfico", command=mostrar_graficos)
    boton_salir = Button(ventana_principal, text="Salir", command=ventana_principal.quit)
    boton_agregar.pack(side="left", expand=True)
    boton_mostrar.pack(side="left", expand=True)
    boton_calcular.pack(side="left",expand=True)
    boton_grafico.pack(side="left",expand=True)
    boton_salir.pack(side="bottom")

    ventana_principal.mainloop()


if __name__ == "__main__":
    main()