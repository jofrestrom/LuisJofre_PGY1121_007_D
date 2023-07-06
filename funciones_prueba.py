import numpy as np
arreglo_esenario = np.empty((10,10), object)
arreglo_esenario.fill("🟩")
lista_ruts = []
lista_filas = []
lista_columnas = []
precio_Platinum =120000
precio_Gold = 80000
precio_Silver = 50000
acumulador = 0
acumPlatinum = 0
acumuladorGold = 0
acumuladorSilver = 0
total_p = 0
total_G = 0
total_S = 0
def mostrar_menu():
    print("""
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")
def validar_opcines():
    while True:
        try:
            opc = int(input("ingrese opcion a ejecutar: "))
            if opc in(1,2,3,4,5):
                return opc
            else:
                print("opcion ingresada incorrecta")
        except:
            print("ERROR!, debe ingresar un  numero entero pocitivo")
def validar_rut():
    while True:
        try:
            rut = int(input("ingrese su rut(sin puntuacion y sin dijito verificador): "))
            if rut >= 1_000_000 and rut <=99_999_999:
                lista_ruts.append(rut)
                return
            else:
                print("rut ingresado no valido")
        except:
            print("debe ingresar un numero entero pocitivo")
def ver_asientos():
    for x in range(10):
        print(f"fila {x+1}|", end=" ")
        for y in range(10):
            print(arreglo_esenario[x][y], end=" ")
        print()
def cant_asientos():
    while True:
        try:
            cant = int(input("ingrese cantidad de asientos: "))
            if cant >= 1 and cant <=3:
                return cant
            else:
                print("cantidad de asientos ingresada incorrecta")
        except:
            print("ERROR!, debe ingresar un  numero entero pocitivo")
def validar_fila():
    while True:
        try:
            fila = int(input("ingrese fila a seleccion: "))
            if fila in(1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("fila ingresada incorrecta")
        except:
            print("ERROR!, debe ingresar un  numero entero pocitivo")
def validar_columna():
    while True:
        try:
            columna = int(input("ingrese columna a seleccion: "))
            if columna >=1 and columna <= 10:
                return columna
            else:
                print("columna ingresada incorrecta")
        except:
            print("ERROR!, debe ingresar un  numero entero pocitivo")

    