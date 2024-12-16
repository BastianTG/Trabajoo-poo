import requests
base_url = 'http://127.0.0.1:8000/api/programmers/'
pokemon_base_url = 'http://127.0.0.1:8000/api/pokemons/'

def create_programmer():
    fullname = input("Ingrese el nombre completo: ")
    nickname = input("Ingrese el apodo: ")
    language = input("Ingrese el lenguaje: ")
    age = int(input("Ingrese la edad: "))
    is_active_input = input("Está activo? (Si/No): ")
    is_active = is_active_input.lower() == 'si'
    data = {
        'fullname': fullname,
        'nickname': nickname,
        'language': language,
        'age': age,
        'is_active': is_active
    }
    response = requests.post(base_url, data=data)
    if response.status_code == 201:
        print("\nProgramador creado exitosamente:", response.json())
    else:
        print("\nError al crear el programador:", response.status_code)

def get_all_programmers():
    response = requests.get(base_url)
    if response.status_code == 200:
        print("\nLista de programadores:")
        for programmer in response.json():
            print(programmer)
    else:
        print("\nError al obtener los programadores:", response.status_code)

def update_programmer():
    programmer_id = int(input("Ingrese el ID del programador a actualizar: "))
    fullname = input("Ingrese el nuevo nombre completo: ")
    nickname = input("Ingrese el nuevo apodo: ")
    language = input("Ingrese el nuevo lenguaje: ")
    age = int(input("Ingrese la nueva edad: "))
    is_active_input = input("Está activo? (Si/No): ")
    is_active = is_active_input.lower() == 'si'
    data = {
        'fullname': fullname,
        'nickname': nickname,
        'language': language,
        'age': age,
        'is_active': is_active
    }
    url = f'{base_url}{programmer_id}/'
    response = requests.put(url, data=data)
    if response.status_code == 200:
        print("\nProgramador actualizado exitosamente:", response.json())
    else:
        print("\nError al actualizar el programador:", response.status_code)

def delete_programmer():
    programmer_id = int(input("Ingrese el ID del programador a eliminar: "))
    url = f'{base_url}{programmer_id}/'
    response = requests.delete(url)
    if response.status_code == 204:
        print("\nProgramador eliminado exitosamente.")
    else:
        print("\nError al eliminar el programador:", response.status_code)

def create_pokemon():
    nombre = input("Ingrese el nombre del Pokémon: ")
    peso = float(input("Ingrese el peso del Pokémon: "))
    tipo = input("Ingrese el tipo del Pokémon: ")
    data = {
        'nombre': nombre,
        'peso': peso,
        'tipo': tipo
    }
    response = requests.post(pokemon_base_url, data=data)
    if response.status_code == 201:
        print("\nPokémon creado exitosamente:", response.json())
    else:
        print("\nError al crear el Pokémon:", response.status_code)

def get_all_pokemon():
    response = requests.get(pokemon_base_url)
    if response.status_code == 200:
        print("\nLista de Pokémon:")
        for pokemon in response.json():
            print(f"- ID: {pokemon['id']}, Nombre: {pokemon['nombre']}, Peso: {pokemon['peso']}, Tipo: {pokemon['tipo']}")
    else:
        print("\nError al obtener los Pokémon:", response.status_code)

def update_pokemon():
    pokemon_id = int(input("Ingrese el ID del Pokémon a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del Pokémon: ")
    peso = float(input("Ingrese el nuevo peso del Pokémon: "))
    tipo = input("Ingrese el nuevo tipo del Pokémon: ")
    data = {
        'nombre': nombre,
        'peso': peso,
        'tipo': tipo
    }
    url = f'{pokemon_base_url}{pokemon_id}/'
    response = requests.put(url, data=data)
    if response.status_code == 200:
        print("\nPokémon actualizado exitosamente:", response.json())
    else:
        print("\nError al actualizar el Pokémon:", response.status_code)

def delete_pokemon():
    pokemon_id = int(input("Ingrese el ID del Pokémon a eliminar: "))
    url = f'{pokemon_base_url}{pokemon_id}/'
    response = requests.delete(url)
    if response.status_code == 204:
        print("\nPokémon eliminado exitosamente.")
    else:
        print("\nError al eliminar el Pokémon:", response.status_code)

def programmer_menu():
    while True:
        print("\n=== Menú CRUD Programadores ===")
        print("1. Crear programador")
        print("2. Ver todos los programadores")
        print("3. Actualizar programador")
        print("4. Eliminar programador")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            create_programmer()
        elif opcion == '2':
            get_all_programmers()
        elif opcion == '3':
            update_programmer()
        elif opcion == '4':
            delete_programmer()
        elif opcion == '5':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")

def pokemon_menu():
    while True:
        print("\nMenú Pokémon")
        print("1. Crear Pokémon")
        print("2. Listar Pokémon")
        print("3. Actualizar Pokémon")
        print("4. Eliminar Pokémon")
        print("5. Volver al Menú Principal")
        option = input("Seleccione una opción: ")

        if option == "1":
            create_pokemon()
        elif option == "2":
            get_all_pokemon()
        elif option == "3":
            update_pokemon()
        elif option == "4":
            delete_pokemon()
        elif option == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
def menu():
    while True:
        print("\nMenú Principal")
        print("1. CRUD Programadores")
        print("2. CRUD Pokémon")
        print("3. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            programmer_menu()
        elif option == "2":
            pokemon_menu()
        elif option == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == '__main__':
    menu()
