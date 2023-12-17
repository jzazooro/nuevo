import csv
import os

def correo_existe(correo):
    if not os.path.isfile('clientes.csv'):
        return False

    with open('clientes.csv', 'r') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Saltar encabezados
        for fila in reader:
            if fila[0] == correo:
                return True
        return False

def registrar_usuario():
    correo = input("Ingrese su correo electrónico: ")
    if correo_existe(correo):
        print("Este correo electrónico ya está registrado. Por favor, use otro.")
        return

    contraseña = input("Ingrese su contraseña: ")
    direccion = input("Ingrese su dirección: ")
    guardar_usuario(correo, contraseña, direccion)
    print("Usuario registrado exitosamente.")

def guardar_usuario(correo, contraseña, direccion):
    existe_archivo = os.path.isfile('clientes.csv')
    with open('clientes.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        if not existe_archivo:
            writer.writerow(['Correo', 'Contraseña', 'Dirección'])  # Encabezados
        writer.writerow([correo, contraseña, direccion])

def iniciar_sesion():
    if not os.path.isfile('clientes.csv'):
        print("No hay usuarios registrados.")
        return

    correo = input("Ingrese su correo electrónico: ")
    contraseña = input("Ingrese su contraseña: ")
    if verificar_usuario(correo, contraseña):
        print("Inicio de sesión exitoso.")
    else:
        print("Correo o contraseña incorrectos, o el usuario no existe.")

def verificar_usuario(correo, contraseña):
    with open('clientes.csv', 'r') as archivo:
        reader = csv.reader(archivo)
        next(reader)  # Saltar encabezados
        for fila in reader:
            if fila[0] == correo and fila[1] == contraseña:
                return True
        return False

