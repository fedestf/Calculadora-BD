import sys
import subprocess as sp
from mysql.connector import MySQLConnection, Error


def conexion():
    db = MySQLConnection(
        host='localhost',
        database='calculadora',
        user='root',
        password='root')
    return db


def testConex(db):
    if db.is_connected():
        print("Conexion establecida")
        input()
    pass

    return


def consultaSuma(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM suma")
    row = cur.fetchall()

    print("- - - - - - - - - - - -")
    for id, calculo, resultado in row:
        print("ID:", id, "|CALCULO:", calculo, "|RESULTADO:", resultado)
        print("- - - - - - - - - - - -")
    pass
    input()
    cur.close()
    db.close()
    return


def consultaResta(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM resta")
    row = cur.fetchall()
    print("- - - - - - - - - - - -")
    for id, calculo, resultado in row:
        print("ID:", id, "|CALCULO:", calculo, "|RESULTADO:", resultado)
        print("- - - - - - - - - - - -")
    pass
    input()
    cur.close()
    db.close()
    return


def consultaMultiplicacion(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM multiplicacion")
    row = cur.fetchall()
    print("- - - - - - - - - - - -")
    for id, calculo, resultado in row:
        print("ID:", id, "|CALCULO:", calculo, "|RESULTADO:", resultado)
        print("- - - - - - - - - - - -")
    pass
    input()
    cur.close()
    db.close()
    return


def consultaDivision(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM division")
    row = cur.fetchall()
    print("- - - - - - - - - - - -")
    for id, calculo, resultado in row:
        print("ID:", id, "|CALCULO:", calculo, "|RESULTADO:", float(resultado))
        print("- - - - - - - - - - - -")
    pass
    input()
    cur.close()
    db.close()
    return


def leerNum():

    dato = int(input("Ingrese un numero: "))
    return dato


def limpiar():

    plataforma = sys.platform
    if plataforma.startswith('linux'):
        sp.call('clear')
    elif plataforma.startswith('win'):
        sp.call('cls', shell=True)
    pass


def suma(a, b):

    res = a+b
    print(a, "+", b, "es :", res)

    return


def resta(a, b):

    res = a-b
    print(a, "-", b, "es :", res)
    return


def division(a, b):
    res = float(a/b)
    print(a, "/", b, "es : ", res)
    return


def multiplicacion(a, b):

    res = a*b
    print(a, "x", b, "es : ", res)

    return


def ingreSuma():  # funcion perfecta
    db = conexion()
    cur = db.cursor()
    a = leerNum()
    b = leerNum()
    resultado = a+b
    calculo = str(a)+"+"+str(b)
    query = "INSERT INTO suma values (null,%(calculo)s,%(resultado)s)"
    datos = {'calculo': calculo, 'resultado': resultado}
    cur.execute(query, datos)
    suma(a, b)
    db.commit()
    db.close()
    pass


def ingreMult():  # funcion perfecta
    db = conexion()
    cur = db.cursor()
    a = leerNum()
    b = leerNum()
    resultado = a*b
    calculo = str(a)+"*"+str(b)
    query = "INSERT INTO multiplicacion values (null,%(calculo)s,%(resultado)s)"
    datos = {'calculo': calculo, 'resultado': resultado}
    cur.execute(query, datos)
    multiplicacion(a, b)
    db.commit()
    db.close()
    pass


def ingreResta():  # funcion perfecta
    db = conexion()
    cur = db.cursor()
    a = leerNum()
    b = leerNum()
    resultado = a-b
    calculo = str(a)+"-"+str(b)
    query = "INSERT INTO resta values (null,%(calculo)s,%(resultado)s)"
    datos = {'calculo': calculo, 'resultado': resultado}
    cur.execute(query, datos)
    resta(a, b)
    db.commit()
    db.close()
    pass


def ingreDiv():  # funcion perfecta
    db = conexion()
    cur = db.cursor()
    a = leerNum()
    b = leerNum()
    resultado = float(a/b)
    calculo = str(a)+"/"+str(b)
    query = "INSERT INTO division values (null,%(calculo)s,%(resultado)s)"
    datos = {'calculo': calculo, 'resultado': resultado}
    cur.execute(query, datos)
    division(a, b)
    db.commit()
    db.close()
    pass
