from asyncore import close_all
import dict_aeropuertos
import os
def StringListToIntList(lista): #Convierte lista de numeros str a int
    resultado = list()
    for item in lista:
        resultado.append(int(item))
    return resultado
def EnterToConinue():
    tmp = input("\nPresione Enter para continuar")
def Opcion1():
    auxPasajeros = dict_aeropuertos.datos['Pasajeros']
    estado = dict_aeropuertos.datos['Estado']
    pasajeros = list()
    # Casting a int32
    for item in auxPasajeros:
        pasajeros.append(int(item))
    lista = list(zip(estado, pasajeros))
    lista.sort(key=lambda x:x[1]) #Ordene la lista, segundo elemento = criterio de ordenamiento
    lista.reverse()
    for i in range(0,5):
        print(lista[i][0],': \n\t\t\t[',lista[i][1],']\n\n')
def Opcion2():
    auxPasajeros = dict_aeropuertos.datos['Pasajeros']
    pasajeros = list()
    # Casting a int32
    pasajeros = StringListToIntList(auxPasajeros)
    print(F'Promedio de pasajeros: {sum(pasajeros)/len(pasajeros):,.2f}')
def Opcion3():
    vuelos_sin = dict_aeropuertos.datos['Vuelos_Sinaloa']
    ciudades = dict_aeropuertos.datos['Ciudad']
    estados = dict_aeropuertos.datos['Estado']
    vuelosPorEstado = list(zip(ciudades,vuelos_sin,estados))
    # Casting a int32
    elementosEliminar = []
    for item in vuelosPorEstado:
        if item[2] == 'Sinaloa':
            elementosEliminar.append(item)

    for item in elementosEliminar:
        vuelosPorEstado.remove(item)

    vuelosPorEstado.sort(key=lambda x:x[1]) #Ordene la lista, segundo elemento = criterio de ordenamiento
    for i in range(0,5):
        print(vuelosPorEstado[i][0],': \n\t\t\t[',vuelosPorEstado[i][1],']')



def Menu():
    os.system('cls')
    op = input("""
    1. 5 aeropuertos con mayor cantidad de pasajeros que desean viajar a Sinaloa.
    2. Promedio de pasajeros.
    3. Los 5 aeropuertos con menos vuelos hacia Sinaloa.
    4. Salir\n\t""")
    os.system('cls')

    if op == '1':
        Opcion1()
    elif op == '2':
        Opcion2()
    elif op == '3':
        Opcion3()
    elif op == '4':
        quit()
    else:
        print("Opcion incorrecta")
    EnterToConinue()



#--------------------------------------------------------------------------------------------------------------------------------
while(True):
    Menu()
