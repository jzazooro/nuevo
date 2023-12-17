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
        o=10+z
        print("La cuenta es de", o, "€")
    
    if m == True and b == True and p == True and e == False:
        o=15+z
        print("La cuenta es de", o, "€")

    if m == True and b == True and p == False and e == True:
        o=15+z
        print("La cuenta es de", o, "€")
    
    if m == True and b == False and p == True and e == True:
        o=15+z
        print("La cuenta es de", o, "€")
    
    if m == True and b == True and p == False and e == False:
        o=20+z
        print("La cuenta es de", o, "€")

    if m == True and b == False and p == True and e == False:
        o=20+z
        print("La cuenta es de", o, "€")
    
    if m == True and b == False and p == False and e == True:
        o=20+z
        print("La cuenta es de", o, "€")
    
    if m == True and b == False and p == False and e == False:
        o=25+z
        print("La cuenta es de", o, "€")

    if m == False and b == True and p == True and e == True:
        o=15+z
        print("La cuenta es de", o, "€")
    
    if m == False and b == True and p == True and e == False:
        o=22.5+z
        print("La cuenta es de", o, "€")

    if m == False and b == True and p == False and e == True:
        o=22.5+z
        print("La cuenta es de", o, "€")
    
    if m == False and b == False and p == True and e == True:
        o=20+z
        print("La cuenta es de", o, "€")
    
    if m == False and b == True and p == False and e == False:
        o=30+z
        print("La cuenta es de", o, "€")

    if m == False and b == False and p == True and e == False:
        o=27.5+z
        print("La cuenta es de", o, "€")
    
    if m == False and b == False and p == False and e == True:
        o=27.5+z
        print("La cuenta es de", o, "€")
    
    if m == False and b == False and p == False and e == False:
        o=35+z
        print("La cuenta es de", o, "€")
        
