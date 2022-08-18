import csv
import os

#gob var
usuario = 'emtech1'
clave = 'papasfritas'

#Funciones generales:
def EnterToContinue():
    tmp = input("\n\t\tPresione \'Enter\' para continuar...")
    os.system('cls')
def login():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if user == usuario and password ==clave:
        return True
    else:
        print("Error, datos no validos")
        EnterToContinue()
        return False

def Menu():
    while True:
        os.system('cls')
        op = input("""
        \t1-.Rutas de importación y exportación
        \t2-.Medio de transporte utilizado
        \t3-.Valor total de importaciones y exportaciones
        \t4-.Salir\n\t\t""")
        os.system('cls')

        if op == "1":
            opcion1()
        elif op == "2":
            opcion2()
        elif op == "3":
            opcion3()
        elif op == "4":
            break
        else:
            print("\t\tOpcion no valida")
        EnterToContinue()

#Basico:
def GetDictionaryWithRutes():
        with open("synergy_logistics_database.csv","r") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            rutasdic = dict()

            for ruta in lector:
                if ruta[3] == "destination":
                    continue
                rutaActual = ruta[2]+"-"+ruta[3]
                if rutaActual in rutasdic:
                    rutasdic[rutaActual] = rutasdic[rutaActual]+1
                else:
                    rutasdic[rutaActual] = 1
            return rutasdic
def GetDictionary_RutesWitchTotal():
    with open("synergy_logistics_database.csv","r") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        rutasdic = dict()
        for ruta in lector:
            if ruta[3] == "destination":
                continue
            rutaActual = ruta[2]+"-"+ruta[3]
            if rutaActual in rutasdic:
               continue
            else:
                rutasdic[rutaActual] = 0

    with open("synergy_logistics_database.csv","r") as archivo:
        lector2 = csv.reader(archivo, delimiter=",")
        for ruta in lector2:
            if ruta[3] == "destination":
                continue
            rutaActual = ruta[2]+"-"+ruta[3]
            rutasdic[rutaActual] += int(ruta[9])
        return rutasdic
def opcion1():
    VentasTotalesPorRuta = GetDictionary_RutesWitchTotal()
    RutasQty = GetDictionaryWithRutes()
    total = GetTotalMoney()
    toprutas = list(zip(VentasTotalesPorRuta.keys(),VentasTotalesPorRuta.values()))
    toprutas.sort(key=lambda x:x[1], reverse = True)
    print("\tPais:\t\t\t\t Total:\t\t\tPorcentaje:")
    for i in range(0,10):
        porcentaje = (toprutas[i][1] / total) * 100
        print(F"""\n\n\t{i+1}-. {toprutas[i][0]}
        \t\t\t\t [ ${toprutas[i][1]} ] \t{porcentaje:,.2f}%
------------------------------------------------------------------------------------------------\n""")
    print("\n\n")
    return RutasQty

#Intermedio:
def GetDicTransportModeWithTotal():
    with open("synergy_logistics_database.csv","r") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        transporte = dict()
        
        for item in lector:
            tipoTransporte = item[7]

            if tipoTransporte == "transport_mode":
                continue

            if tipoTransporte in transporte:
                transporte[tipoTransporte] += int(item[9])
            else:
                transporte[tipoTransporte] = int(item[9])
        return transporte
def GetTotalMoney():
    with open("synergy_logistics_database.csv","r") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        sumatoria = 0
        
        for item in lector:
            #Evita la cabecera de las columnas
            if item[9] == "total_value":
                continue
            else:
                sumatoria += int(item[9])
        return sumatoria            
def opcion2():
    auxdic = GetDicTransportModeWithTotal()
    total = GetTotalMoney()
    print("\n\n\tTipo de transporte:\t\tDinero generado")
    transportes = list(zip(auxdic.keys(),auxdic.values()))
    contador = 0
    for t,c in transportes:
        contador += 1
        if contador>3:
            break
        print(F"""
        {contador}-. {t}: \n \t    [{((c/total)*100):,.2f}%] \t\t\t\t $ {c}
        -----------------------------------------------------------------------\n\n""")

#Avanzado:
def GetDicPaisesWithTotal():
    with open("synergy_logistics_database.csv","r") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        paises = dict()
        
        for item in lector:
            pais = item[2]
            #Evita la cabecera de las columnas
            if pais == "origin":
                continue
            
            if pais in paises: #Suma el valor al valor actual del diccionario
                paises[pais] += int(item[9])
            else: #Agrega el pais al diccionario y le agrega el valor de la venta actual
                paises[pais] = int(item[9])
        return paises
def Get80Porcent(paises):
    paises.sort(key=lambda x: x[1], reverse=True)
    porcentajeAcumulado = 0
    print("Paises: ")
    i = 0
    #Muestra los paises (orden ascendente) con su porcentaje y va sumando el porcentaje de los paises
    for pais, porc in paises:
        i += 1
        if porcentajeAcumulado>80:
            pais = pais + " [PAIS DESENFOCADO]"
        porcentajeAcumulado += porc
        print(F"""\t{i}-. {pais} \n\t\t\t\t[{porc:,.2f}%]
    ---------------------------------------------------------------

    \t\t\t\t\t\t\t\t___________________
    \t\t\t\t\t\t\t\tSumatoria: {porcentajeAcumulado:,.2f} %\n""")
def opcion3():
    aux = GetDicPaisesWithTotal()
    paises = list(zip(aux.keys(),aux.values()))
    paises.sort(key=lambda x:x[1], reverse=True)
    GananciasTotales = GetTotalMoney()
    porcentaje = 0
    paises_porcentaje = []
    #Crear una lista con porcentajes
    for pais, qty in paises:
        porcentaje = (qty/ GananciasTotales) * 100
        paises_porcentaje.append([pais,porcentaje])
    #Mostrara los datos con sumatoria total debajo
    Get80Porcent(paises_porcentaje)


######################################################################################################################################
while login() == False:
    os.system("cls")
Menu()