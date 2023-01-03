import math
import random

def leer_numero(ini,fin,mensaje):
    while True:
        print(mensaje,end=" ")
        try:
            dato = int(input())
        except:
            print("Error: Tipo de dato no válido")
        if(dato>=ini and dato<=fin):
            return dato

def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quiere generar? [1-20]:")
    modo = leer_numero(1,3,"¿De qué modo quiere redondear los numeros? [1] Al alza [2] A la baja [3] Normal")
    listaAleatorios = []

    for i in range(numeros):
        NumeroAleatorio = random.uniform(0,100)
        if(modo == 1):
            NumeroRedondeado = math.trunc(NumeroAleatorio)+1
            listaAleatorios.append(NumeroRedondeado)
        elif(modo == 2):
            NumeroRedondeado = math.trunc(NumeroAleatorio)
            listaAleatorios.append(NumeroAleatorio)
        else:
            NumeroRedondeado = NumeroAleatorio
            listaAleatorios.append(NumeroAleatorio)
        print("El número generado aleatorio es:",NumeroAleatorio,"El número redondeado sería:",NumeroRedondeado)
    return listaAleatorios
generador()