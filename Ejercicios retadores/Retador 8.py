import os
pasajeros = [] # [nombre , edad, destino]
closeMenu = False
numerox = 12
vuelosTotales = [('BJX',0), ('GDL',0),('JAL',0)]
edadPromedio = [('BJX',0), ('GDL',0),('JAL',0)]
JAL = 'JAL'
BJX = 'BJX'
GDL = 'GDL'
# clientes = {} # id : lista[nombre, edad, destino, clientepreferente(true,false)]
clientes = {45471:["Luis Perez",45,BJX, True], 8944411:["Fernanda Garcia",25,JAL, True],
15223:["Alejandra Ortiz",33,GDL, True]}


#Cuestiones visuales-----------------------------------------
def ShowMenu():
    os.system('cls')
    option = int(input('(1) Agregar cliente  \n(2) Listar todos los clientes \n(3) Listar clientes preferentes \n(4) Salir\n'))
    os.system('cls')

    if option == 1:
        AddCliente()
    elif option == 2:
        showClientes()
    elif option == 3:
        ShowClientesPreferentes()
    elif option == 7:
        closeMen = True
    else:
        EnterToContinue()
        tmp = input("Error, opcion no valida")
def EnterToContinue():
    tmp = input("Pulse Enter para continuar")

def ShowEdadAVG(): # debe ejecutarse despues de vuelosTotales (tiene dependencia)
    SumatoriaEdades = {'BJX':0,'GDL':0,'JAL':0}
    for pasajero in pasajeros:
        for destino in vuelosTotales:
            if pasajero[2].upper() == destino[0].upper():
                SumatoriaEdades[destino[0]] = SumatoriaEdades[destino[0]] + pasajero[1]
                break

    vuelototalesdic = dict(vuelosTotales)
    resultadosfinales = []
    for item in edadPromedio:
        if vuelototalesdic[item[0]] != 0:
            aux = (item[0],(SumatoriaEdades[item[0]] / vuelototalesdic[item[0]]))
            resultadosfinales.append(aux)
        else:
            aux = (item[0],0)
            resultadosfinales.append(aux)


    
    print("\n\nDestino \tPromedio")
    for item in resultadosfinales:
        print(str(item[0]) + "\t\t" + str(item[1]))
    return
def AddCliente():
    while(True):
        os.system('cls')
        nombre = input("Nombre: ")
        if nombre.upper() == "X":
            break
        ID = int(input("Ingrese el ID-INE: "))
        edad = int(input("Edad: "))
        IATA = input("Destino: ")
        IsPreferent = False
        while(True):
            Preferent = str(input("S para preferente, \'n\' no preferente: "))
            if Preferent.upper() == 'S':
                IsPreferent = True
                break
            elif Preferent.upper() == 'N':
                IsPreferent = False
                break
            else:
                temp = input("Error, presione \'Enter\' para continuar")                
        vuelo = [nombre,edad,IATA,IsPreferent]
        addVuelo(vuelo)
        clientes[ID] = vuelo
def addVuelo(des):
    for item in vuelosTotales:
        if item[0] == str(des).upper():
            aux = (item[0],item[1] + 1)
            vuelosTotales.remove(item)
            vuelosTotales.append(aux)
            break
def showVuelos():
    print("Destino\t\tCantidad:")
    for item in vuelosTotales:
        print(str(item[0]) + ":\t\t" + str(item[1]))
def showClientes():
    for id,cliente in list(zip(clientes.keys(),clientes.values())):
        print(id,':  ',cliente)
def ShowClientesPreferentes():
    for id, cliente in list(zip(clientes.keys(),clientes.values())):
        if cliente[-1] == True:
             print('ID: ', id,' ',cliente)
def DeleteClient():
    try:
        ID = int(input('Ingrese el ID: '))
        if ID in clientes.keys():
            del clientes[ID]
            print("Cliente eliminado")
        else:
            print("No existe ningun cliente con ese ID")
    except:
        print('Error, entrada no valida')
def AVGClients():
    lista = clientes.values()
    edades = list()
    for element in lista:
        edades.append(element[1])
    print(F'Edad promedio: {sum(edades)/len(edades):,.2f}')
def AVGPreferentClients():
    lista = clientes.values()
    edades = list()
    for element in lista:
        # print(element[3])
        if element[3]:
            edades.append(element[1])
    print(F'\n\tEdad promedio de los clientes preferentes: {sum(edades)/len(edades):,.2f}\n')


while(closeMenu == False):
    # ShowMenu()
    
    os.system('cls')
    option = int(input("""
    (1) Agregar cliente  
    (2) Listar todos los clientes 
    (3) Listar clientes preferentes
    (4) Eliminar cliente
    (5) Mostrar la edad promedio de todos los clientes
    (6) Mostrar la edad promedio de los clientes preferentes
    (7) Salir\n\t"""))
    os.system('cls')

    if option == 1:
        AddCliente()
    elif option == 2:
        showClientes()
    elif option == 3:
        ShowClientesPreferentes()
    elif option == 4:
        DeleteClient()
    elif option == 5:
        AVGClients()
    elif option == 6:
        AVGPreferentClients()
    elif option == 7:
        closeMenu = True
        break
    else:
        print("Error, opcion no valida")

    EnterToContinue()
    





# showClientes()
# showVuelos()
# ShowEdadAVG()


