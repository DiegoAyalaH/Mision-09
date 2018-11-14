#Diego Armando Ayala Hernández
#A01376727
#Misión 9:Listas segunda parte

#Random para generar numeros al azar para las listas
from random import randint

#Función que quita los pares de las listas
def extraerPares(listaOriginal):
    listaNueva = []
    for n in listaOriginal:
        if n % 2 == 0:
            listaNueva.append(n)
    return listaNueva
#Genera una lista que regresa los valores mayores
def extraerMayoresPrevio(listaOriginal):
    listaNueva = []
    for n in range(1, len(listaOriginal)-1):
        if listaOriginal[n] > listaOriginal[n-1]:
            listaNueva.append(listaOriginal[n])
    return listaNueva
#Función qu eintercambia de lugar ciertos valores
def intercambiarParejas(listaOriginal):
    listaNueva = []
    for n in range(1, len(listaOriginal) - 1, 2):
        listaNueva.append(listaOriginal[n])
        listaNueva.append(listaOriginal[n - 1])
    if len(listaOriginal) % 2 == 1:
        listaNueva.append(listaOriginal[len(listaOriginal)-1])
    return listaNueva
#Función que intercambia de lugar el número mayor y el menor
def intercambiarMM(listaOriginal):
    menor = listaOriginal[0]
    mayor = listaOriginal[len(listaOriginal)-1]
    listaOriginal[len(listaOriginal)-1] = menor
    listaOriginal[0] = mayor
    return listaOriginal
#Función que promedia los numeros de enmedio sin considerar los extremos
def promediarCentro(listaOriginal):
    listaNueva = listaOriginal.copy()
    listaNueva.sort()
    listaNueva.pop(0)
    listaNueva.reverse()
    listaNueva.pop(0)
    listaNueva.reverse()
    acumulador = 0
    for x in listaNueva:
        acumulador += x
    return acumulador // len(listaNueva)
#saca la desviación y promedio de la lista
def calcularEstadistica(listaOriginal):
    acumulador = 0
    for n in range(0, len(listaOriginal) - 1):
        acumulador += listaOriginal[n]
    media = acumulador / len(listaOriginal)
    for n in range(0, len(listaOriginal) - 1):
        acumulador += listaOriginal[n]-media
    acumulador = acumulador**2
    acumulador = acumulador / (len(listaOriginal)-1)
    desviacion = acumulador**.5
    return media, desviacion
    

#función main
def main():
    lista1 = [randint(0, 100) for x in range(0, 15)]
    lista2 = [randint(0, 100) for x in range(0, 20)]
    lista3 = [randint(0, 100) for x in range(0, 30)]
    lista4 = [randint(0, 100) for x in range(0, 10)]

    print("Ejercicio 1: pares")
    print("-------------------------------------------------------------------------")
    print("lista orginal %s, lista resultante %s." % (lista1, extraerPares(lista1)))
    print("lista orginal %s, lista resultante %s." % (lista2, extraerPares(lista2)))
    print("lista orginal %s, lista resultante %s." % (lista3, extraerPares(lista3)))
    print("lista orginal %s, lista resultante %s." % (lista4, extraerPares(lista4)))
    print("")
    print("Ejercicio 2 : mayores previos")
    print("-------------------------------------------------------------------------")
    print("lista orginal %s, lista resultante %s." % (lista1, extraerMayoresPrevio(lista1)))
    print("lista orginal %s, lista resultante %s." % (lista2, extraerMayoresPrevio(lista2)))
    print("lista orginal %s, lista resultante %s." % (lista3, extraerMayoresPrevio(lista3)))
    print("lista orginal %s, lista resultante %s." % (lista4, extraerMayoresPrevio(lista4)))
    print("")
    print("Ejercicio 3: intercambiar Parejas")
    print("-------------------------------------------------------------------------")
    print("lista orginal %s, lista resultante %s." % (lista1, intercambiarParejas(lista1)))
    print("lista orginal %s, lista resultante %s." % (lista2, intercambiarParejas(lista2)))
    print("lista orginal %s, lista resultante %s." % (lista3, intercambiarParejas(lista3)))
    print("lista orginal %s, lista resultante %s." % (lista4, intercambiarParejas(lista4)))
    print("")
    print("Ejercicio 4 : intercambiar MM")
    print("-------------------------------------------------------------------------")
    print("lista orginal %s, lista resultante %s." % (lista1, intercambiarMM(lista1)))
    print("lista orginal %s, lista resultante %s." % (lista2, intercambiarMM(lista2)))
    print("lista orginal %s, lista resultante %s." % (lista3, intercambiarMM(lista3)))
    print("lista orginal %s, lista resultante %s." % (lista4, intercambiarMM(lista4)))
    print("")
    print("Ejercicio5 promediar centro")
    print("-------------------------------------------------------------------------")
    print("lista orginal %s, lista resultante %s." % (lista1, promediarCentro(lista1)))
    print("lista orginal %s, lista resultante %s." % (lista2, promediarCentro(lista2)))
    print("lista orginal %s, lista resultante %s." % (lista3, promediarCentro(lista3)))
    print("lista orginal %s, lista resultante %s." % (lista4, promediarCentro(lista4)))
    print("")
    print("Ejercicio 6 calcularEstadistica")
    print("-------------------------------------------------------------------------")
    print("lista orginal %s, lista resultante %s." % (lista1, calcularEstadistica(lista1)))
    print("lista orginal %s, lista resultante %s." % (lista2, calcularEstadistica(lista2)))
    print("lista orginal %s, lista resultante %s." % (lista3, calcularEstadistica(lista3)))
    print("lista orginal %s, lista resultante %s." % (lista4, calcularEstadistica(lista4)))
    print("")

main()
