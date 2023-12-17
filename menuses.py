import os
import csv

def mostrar_y_elegir_opciones(opciones, caracteristica):
    while True:
        print(f"Elige tu {caracteristica}:")
        for idx, opcion in enumerate(opciones, start=1):
            print(f"{idx}. {opcion}")
        try:
            eleccion = int(input("Selecciona una opción: "))
            if 1 <= eleccion <= len(opciones):
                return opciones[eleccion - 1]
            else:
                print("Por favor, elige una opción válida.")
        except ValueError:
            print("Por favor, introduce un número.")

def mostrar_y_elegir_multiples_opciones(opciones, caracteristica):
    while True:
        print(f"Elige tus {caracteristica} (separa los números con comas y sin espacios):")
        for idx, opcion in enumerate(opciones, start=1):
            print(f"{idx}. {opcion}")
        entrada = input("Selecciona las opciones: ")
        try:
            elecciones = [int(e.strip()) for e in entrada.split(',')]
            if all(1 <= e <= len(opciones) for e in elecciones):
                return [opciones[e - 1] for e in elecciones]
            else:
                print("Por favor, elige opciones válidas.")
        except ValueError:
            print("Por favor, introduce números válidos separados por comas.")

def elegir_menu():
    menus = ["Si", "No"]
    return mostrar_y_elegir_opciones(menus, "menu")


def elegir_bebida():
    bebidas = ["Agua", "Refresco", "Cerveza artesanal", "Vino de la casa", "Domaine de la Romanée-Conti", "Château Lafite Rothschild", "Nada"]
    return mostrar_y_elegir_opciones(bebidas, "bebida")

def elegir_postre():
    postres = ["Banana Split", "Weed Brownie", "Fruta", "Nada"]
    return mostrar_y_elegir_opciones(postres, "postre")

def elegir_entrante():
    entrantes = ["Nachos Guerrero", "Croquetas de cocidito madrileño", "Nada"]
    return mostrar_y_elegir_opciones(entrantes, "entrante")

def guardar_pedido(menu, tamaño, masa, ingredientes, salsa, tecnica_coccion, presentacion, bebida, postre, entrante):
    existe_archivo = os.path.isfile('pedidos.csv')
    with open('pedidos.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        if not existe_archivo:
            writer.writerow(['Menu', 'Tamaño', 'Masa', 'Ingredientes', 'Salsa', 'Técnica de Cocción', 'Presentación', 'Bebida', 'Postre', 'Entrante'])
        writer.writerow([menu, tamaño, masa, ', '.join(ingredientes), salsa, tecnica_coccion, presentacion, bebida, postre, entrante])
    print("Pedido guardado exitosamente.")

def crear_pedido():
    menus = ["Si", "No"]
    tamaños = ["Pequeña", "Mediana", "Familiar"]
    masas = ["Fina", "Clasica", "Rellena"]
    ingredientes = ["Tomate", "Queso", "Jamon", "Piña", "Carne picada", "Aceitunas  ", "Pepperoni", "Champiñones", "Jalapeños", "Extra queso"]
    salsas = ["Picante", "Carbonara", "Barbacoa"]
    tecnicas_coccion = ["Horno de leña", "Horno convencional"]
    presentaciones = ["Normal", "Sin borde", "Borde de queso"]

    menu = mostrar_y_elegir_opciones(menus, "menú")
    tamaño = mostrar_y_elegir_opciones(tamaños, "tamaño")
    masa = mostrar_y_elegir_opciones(masas, "masa")
    ingredientes_seleccionados = mostrar_y_elegir_multiples_opciones(ingredientes, "ingredientes")
    salsa = mostrar_y_elegir_opciones(salsas, "salsa")
    tecnica_coccion = mostrar_y_elegir_opciones(tecnicas_coccion, "técnica de cocción")
    presentacion = mostrar_y_elegir_opciones(presentaciones, "presentación")
    bebida = elegir_bebida()
    postre = elegir_postre()
    entrante = elegir_entrante()

    print("\nTu pedido completo:")
    print(f"Pizza - Tamaño: {tamaño}, Masa: {masa}, Ingredientes: {', '.join(ingredientes)}, Salsa: {salsa}, Técnica de cocción: {tecnica_coccion}, Presentación: {presentacion}")
    print(f"Bebida: {bebida}, Postre: {postre}, Entrante: {entrante}")

    guardar_pedido(menu, tamaño, masa, ingredientes_seleccionados, salsa, tecnica_coccion, presentacion, bebida, postre, entrante)

def menu_ordenar_pizza():
    while True:
        print("\nBienvenido a la Pizzería - Menú de Personalización de Pizza")
        print("1. Crear Pizza Personalizada")
        print("2. Ver la carta")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_pedido()
            break
        elif opcion == '2':
            print("1. Carta de menus")
            print("2. Carta individual")
            print("NOTA \n")
            print("El vino Domaine de la Romanée-Conti implica un suplemento de 1000€ \n")
            print("Seleccion de nuestros editores. Le recomendamos el Château Lafite Rothschild y las croquetas de cocidito madrileño \n")
            seleccion = input("Seleccione una opción: \n")
            if seleccion == '1':
                print("Menu (Entrante, Pizza, Postre, Bebida): 25€ \n")
                print("Menu (Entrante, Pizza, Postre): 20€ \n")
                print("Menu (Entrante, Pizza, Bebida): 20€ \n")
                print("Menu (Pizza, Postre, Bebida): 20€ \n")
                print("Menu (Entrante, Pizza): 15€ \n")
                print("Menu (Pizza, Bebida): 15€ \n")
                print("Menu (Pizza, Postre): 15€ \n")
                print("Menu (Pizza): 10€ \n")
            if seleccion == '2':
                print("Pizza: 15€ \n")
                print("Entrante: 7.5€ \n")
                print("Postre: 7.5€ \n")
                print("Bebida: 5€ \n")

        
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")



