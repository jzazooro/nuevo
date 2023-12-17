from usuario import *
from menuses import *
from calculadora import *
from notificador import *

import csv
import os

def main():

    while True:
        print("\nBienvenido a la Pizzería")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
            menu_ordenar_pizza()
            calculin()
            sistema_promociones = SistemaPromociones()

            archivo_csv = 'clientes.csv' 

            listo = None

            with open(archivo_csv, 'r') as file:
                csv_reader = csv.reader(file)

                for fila in csv_reader:
                    listo = fila

            sujeto = listo[0]

            cliente1 = Cliente(sujeto)

            sistema_promociones.subscribe(cliente1)

            sistema_promociones.agregar_promocion("30% de descuento en tu próxima compra")


        elif opcion == '3':
            break
        else:
            print("Opción no válida.")

main()