from funciones import *
from menu import *

salir = False

while salir == False:
    mostrarMenu()
    opc = int(input("Ingrese Opcion : "))

    if opc == 1:
        limpiar()
        print("---------- SUMA")
        ingreSuma()
        input()
        limpiar()
        pass
    if opc == 2:
        limpiar()
        print("---------- RESTA")
        ingreResta()
        input()
        limpiar()
        pass

    if opc == 3:
        limpiar()
        print("----------- DIVISION")
        ingreDiv()
        input()
        limpiar()
        pass

    if opc == 4:
        limpiar()
        print("----------- MULTIPLICACION")
        ingreMult()
        input()
        limpiar()
        pass

    if opc == 5:
        salir2 = False
        while salir2 == False:
            menuConsultas()
            opc2 = int(input("Seleccione opcion: "))

            if opc2 == 1:
                db = conexion()
                consultaSuma(db)
                pass

            if opc2 == 2:
                db = conexion()
                consultaResta(db)
                pass
            if opc2 == 3:
                db = conexion()
                consultaDivision(db)
                pass
            if opc2 == 4:
                db = conexion()
                consultaMultiplicacion(db)
                pass

            if opc2 == 0:
                salir2 = True
                limpiar()
                pass
        pass
    pass

    if opc == 0:
        print("Arios iriotas")
        input()
        exit()
        salir = True
        limpiar()

        pass
pass
