
import os
import time
import msvcrt
from funciones_prueba import *
while True:
    os.system('cls')
    mostrar_menu()
    opc = validar_opcines()
    if opc == 1:
        if "🟩" not in arreglo_esenario:
            print("todos los asiento fueron ocupados en su totalidad")
            time.sleep(2)
            continue
        rut = validar_rut()
        if rut in lista_ruts:
            print("rut ya registrado")
            time.sleep(2)
            continue
        cant = cant_asientos()
        for e in range(cant):
            while True:
                os.system('cls')
                ver_asientos()
                print("""
            Platinum, $120.000. (Asientos del 1 al 20).
            Gold, $80.000. (Asientos del 21 al 50).
            Silver, $50.000. (Asientos del 51 al 100.).""")
                fila = validar_fila()
                colum = validar_columna()
                if arreglo_esenario[fila-1][colum-1]=="🟩":
                    arreglo_esenario[fila-1][colum-1] = "🟥"
                    print("asiento comprado con exito")
                    print("precione una tecla para confirmar")
                    msvcrt.getch()
                    lista_filas.append([fila-1])
                    lista_columnas.append([colum-1])
                    break
                else:
                    print("asiento ocupado")
            if fila >= 1 and fila <= 2:
                acumPlatinum += 1
                total_p += acumPlatinum*precio_Platinum
            elif fila >= 3 and fila <= 5:
                acumuladorGold += 1
                total_G += acumuladorGold*precio_Gold
            elif fila >=6 and fila <= 10:
                acumuladorSilver += 1
                total_S += acumuladorSilver*precio_Silver
    elif opc == 2:
        ver_asientos()
        print("precione una tecla para continuar")
        msvcrt.getch()
    elif opc == 3:
        for h in range(len(lista_ruts)):
            print(lista_ruts[h])
        print("precione una tecla para continuar")
        msvcrt.getch()
    elif opc == 4:
        print(f"""las ganancias totales son: 
        entrada  | cantidad | total
        Platinum | {acumPlatinum}\t|{total_p} 
        Gold     | {acumuladorGold}\t|{total_G}
        Silver   | {acumuladorSilver}\t|{total_S}
        TOTAL DE GANANCIAS:{total_p+total_G+total_S}
        TOTAL DE ENTRADAS COMPRADAS: {acumPlatinum+acumuladorGold+acumuladorSilver}""")
        print("precione una tecla para continuar")
        msvcrt.getch()
    else:
        time.sleep(2)
        print("""
        nombre: luis jofre
        fecha: 06/07/2023""")
        time.sleep(3)
        break