pasajeros = [] # [nombre , edad, destino]
vuelosTotales = [('BJX',0), ('GDL',0),('JAL',0)]
edadPromedio = [('BJX',0), ('GDL',0),('JAL',0)]
import os
def addVuelo(des):
    for item in vuelosTotales:
        if item[0] == str(des).upper():
            aux = (item[0],item[1] + 1)
            vuelosTotales.remove(item)
            vuelosTotales.append(aux)
            break
    return
def showVuelos():
    print("Destino\t\tCantidad:")
    for item in vuelosTotales:
        print(str(item[0]) + ":\t\t" + str(item[1]))
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



while(True):
    nombre = input("Nombre: ")
    if nombre.upper() == "X":
        break
    edad = int(input("Edad: "))
    IATA = input("Destino: ")
    newtup = (nombre,edad,IATA)
    pasajeros.append(newtup)
    addVuelo(IATA)
    print("\n\n")
os.system("cls")
showVuelos()
ShowEdadAVG()


