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

    if orden[-3] == "Domaine de la Romanée-Conti":
        z=995
    else:
        z=0

    if orden[-2] == "Nada":
        p = True
    else:
        p = False

    if orden[-1] == "Nada":
        e = True
    else:
        e = False

    if m == True and b == True and p == True and e == True:
        o=30+z
        print("La cuenta es de", o, "€")
    
    if m == True and b == True and p == True and e == False:
        o=22.5+z
        print("La cuenta es de 22.5€")

    if m == True and b == True and p == False and e == True:
        o=22.5+z
        print("La cuenta es de 22.5€")
    
    if m == True and b == False and p == True and e == True:
        o=25+z
        print("La cuenta es de 25€")
    
    if m == True and b == True and p == False and e == False:
        o=17.5+z
        print("La cuenta es de 17.5€")

    if m == True and b == False and p == True and e == False:
        o=20+z
        print("La cuenta es de 20€")
    
    if m == True and b == False and p == False and e == True:
        o=20+z
        print("La cuenta es de 20€")
    
    if m == True and b == False and p == False and e == False:
        o=15+z
        print("La cuenta es de 15€")

    if m == False and b == True and p == True and e == True:
        o=20+z
        print("La cuenta es de 20€")
    
    if m == False and b == True and p == True and e == False:
        o=12.5+z
        print("La cuenta es de 12.5€")

    if m == False and b == True and p == False and e == True:
        o=12.5+z
        print("La cuenta es de 12.5€")
    
    if m == False and b == False and p == True and e == True:
        o=15+z
        print("La cuenta es de 15€")
    
    if m == False and b == True and p == False and e == False:
        o=5+z
        print("La cuenta es de 5€")

    if m == False and b == False and p == True and e == False:
        o=7.5+z
        print("La cuenta es de7.55€")
    
    if m == False and b == False and p == False and e == True:
        o=7.5+z
        print("La cuenta es de 7.5€")
    
    if m == False and b == False and p == False and e == False:
        print("La cuenta es de 0€, vete a tomar el pelo a otro local")
