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
        print(f"Elige tus {caracteristica} (separa los números con comas):")
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

def guardar_pedido(tamaño, masa, ingredientes, salsa, tecnica_coccion, presentacion):
    existe_archivo = os.path.isfile('pedidos.csv')
    with open('pedidos.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        if not existe_archivo:
            writer.writerow(['Tamaño', 'Masa', 'Ingredientes', 'Salsa', 'Técnica de Cocción', 'Presentación'])
        writer.writerow([tamaño, masa, ', '.join(ingredientes), salsa, tecnica_coccion, presentacion])
    print("Pedido guardado exitosamente.")

def crear_pizza():
    tamaños = ["Pequeña", "Mediana", "Grande"]
    masas = ["Delgada", "Gruesa", "Artesanal"]
    ingredientes = ["Pepperoni", "Champiñones", "Jalapeños", "Extra queso"]
    salsas = ["Tomate", "Albahaca", "Barbacoa"]
    tecnicas_coccion = ["Horno de leña", "Horno convencional"]
    presentaciones = ["Normal", "Sin borde", "Borde de queso"]

    tamaño = mostrar_y_elegir_opciones(tamaños, "tamaño")
    masa = mostrar_y_elegir_opciones(masas, "masa")
    ingredientes_seleccionados = mostrar_y_elegir_multiples_opciones(ingredientes, "ingredientes")
    salsa = mostrar_y_elegir_opciones(salsas, "salsa")
    tecnica_coccion = mostrar_y_elegir_opciones(tecnicas_coccion, "técnica de cocción")
    presentacion = mostrar_y_elegir_opciones(presentaciones, "presentación")

    print("\nTu pizza personalizada:")
    print(f"Tamaño: {tamaño}, Masa: {masa}, Ingredientes: {', '.join(ingredientes_seleccionados)}, Salsa: {salsa}, Técnica de cocción: {tecnica_coccion}, Presentación: {presentacion}")
    guardar_pedido(tamaño, masa, ingredientes_seleccionados, salsa, tecnica_coccion, presentacion)

# Menú para ordenar pizza
def menu_ordenar_pizza():
    while True:
        print("\nBienvenido a la Pizzería - Menú de Personalización de Pizza")
        print("1. Crear Pizza Personalizada")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_pizza()
        elif opcion == '2':
            break
        else:
            print("Opción no válida.")

# Llamada al menú principal aquí
if __name__ == "__main__":
    menu_ordenar_pizza()
