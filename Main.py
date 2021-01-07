import Funciones

n=""
while n!="s" :
    n=input("Ingrese opcion: s para salir, Enter continuar :")
    if n=="s" :
        break
    Funciones.nombres()
    Funciones.numero()
print()
print("--------Detalle-----------------")
print()
print ("Nombres    Números Factoriales")
Funciones.listar_datos()
print()
print("---------Resumen------------------")
print()
Funciones.resumen()
