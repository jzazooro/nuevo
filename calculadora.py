import csv

def calculin():

    archivo_csv = 'pedidos.csv' 

    orden = None

    with open(archivo_csv, 'r') as file:
        csv_reader = csv.reader(file)

        for fila in csv_reader:
            orden = fila

    if orden[0].lower() == "si":
        m = True
    else:
        m = False

    if orden[-3] == "Nada":
        b = True
    else:
        b = False

    if orden[-2] == "Nada":
        p = True
    else:
        p = False

    if orden[-1] == "Nada":
        e = True
    else:
        e = False

    if m == True and b == True and p == True and e == True:
        print("La cuenta es de 25€")
    
    if m == True and b == True and p == True and e == False:
        print("La cuenta es de 20€")

    if m == True and b == True and p == False and e == True:
        print("La cuenta es de 20€")
    
    if m == True and b == False and p == True and e == True:
        print("La cuenta es de 20€")
    
    if m == True and b == True and p == False and e == False:
        print("La cuenta es de 15€")

    if m == True and b == False and p == True and e == False:
        print("La cuenta es de 15€")
    
    if m == True and b == False and p == False and e == True:
        print("La cuenta es de 15€")
    
    if m == True and b == False and p == False and e == False:
        print("La cuenta es de 10€")

calculin()