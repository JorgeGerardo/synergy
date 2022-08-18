import os
from statistics import stdev
IsMenuOpen = True
meses = ['Enero    ','Febrero  ','Marzo    ','Abril    ','Mayo     ','Junio    ','Julio    '
,'Agosto   ','September','October  ','November ','December ']
ventas_anuales = {2010: (69, 49, 10, 99, 96, 16, 2, 41, 36, 10, 45, 43),
 2011: (53, 63, 88, 81, 37, 47, 34, 11, 54, 19, 35, 71),
 2012: (5, 3, 40, 25, 32, 50, 61, 56, 73, 51, 30, 65),
 2013: (40, 100, 4, 41, 28, 99, 20, 96, 78, 76, 68, 97), #anio mayor ventas
 2014: (7, 25, 33, 47, 48, 37, 46, 39, 48, 68, 28, 90)}
#Utilidades
def EnterToContinue():
    tmp = input("\n\n\t\tEnter to continue: ")
    os.system('cls')
def VerificarAnio(anio):
    anioInt = int(anio)
    anios = ventas_anuales.keys()
    if anioInt in anios:
        return True
    else:
        return False


#Option 1
def InformacionAnio():
    anioSeleccinoado = input("Ingrese el año deseado: ")
    os.system('cls')
    if VerificarAnio(anioSeleccinoado):
        consulta = list(ventas_anuales[int(anioSeleccinoado)])
        for mes,cantidad in list(zip(meses,consulta)):
            print('\t',mes,': ',cantidad)
    else:
        print("No existen datos sobre el año ingresado")

#Option 2
def AgregarInformacion():
    anioSeleccinoado = input("Ingrese el año para agregar informacion: ")
    os.system('cls')
    if VerificarAnio(anioSeleccinoado):
        print("No existen datos sobre el año ingresado")
    else:
        ventas = []
        for i in range(0,12):
            venta = input(F'Ingrese el numero de ventas de {meses[i]}: ')
            # if venta.upper() == 'X':
            #     break
            ventas.append(int(venta))
        ventas_anuales[int(anioSeleccinoado)] = ventas
        x = 12
            
#Option 3
def AnalisisEstadistico():
    anioSeleccinoado = input("Ingrese el año para agregar informacion: ")
    os.system('cls')
    if VerificarAnio(anioSeleccinoado):
        print(F'Analisis estadistico: {str(anioSeleccinoado)}:\n')
        print(F'Total:      { sum(ventas_anuales[int(anioSeleccinoado)])}')
        print(F'Promedio:   { round(sum(ventas_anuales[int(anioSeleccinoado)])/len(ventas_anuales),2)}')
        print(F'Maximo:     { max(ventas_anuales[int(anioSeleccinoado)])}')
        print(F'Minimo:     { min(ventas_anuales[int(anioSeleccinoado)])}')
        print(F'Desviacion: { round(stdev(ventas_anuales[int(anioSeleccinoado)]),2)}')
    else:
        print("No existen datos sobre el año ingresado")

#Option 4
def Reporte():
    anios = ventas_anuales.keys()
    mayorAnio = 0 #Primer elemento de la lista
    totalMayorAnio = 0
    for anio in anios:
        totalAnio = sum(ventas_anuales[int(anio)])
        if totalAnio > totalMayorAnio:
            mayorAnio = anio
            totalMayorAnio = totalAnio
    print('El año con mayores ventas es: ',mayorAnio)
    print(F'Ventas totales: {sum(ventas_anuales[int(mayorAnio)])}')

    


def ShowMenu():
    op = input("""
    \t1 Informacion por año
    \t2 Agregar informacion
    \t3 Realizar analisis
    \t4 Generar reporte año con mayores ventas\n\t""")
    os.system('cls')
    Menu(op)
def Menu(option):
    if option == '1':
        InformacionAnio()
    elif option == '2':
        AgregarInformacion()
    elif option == '3':
        AnalisisEstadistico()
    elif option == '4':
        Reporte()
    elif option == '5':
        IsMenuOpen = False
    else:
        print("Opcion incorrecta")


while(IsMenuOpen):
    ShowMenu()
    EnterToContinue()



