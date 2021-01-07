
import os
os.system('cls')

valor=0
diccionario_nombre=[]
diccionario_factorial=[]
datos_nombre=[]
datos_factorial=[]

def nombres():
    diccionario_nombre=[]
    nombre = str(input ("Ingresar Nombre    "))
    print ('nombre : ',nombre)
    diccionario_nombre.append(nombre)
    datos_nombre.append(diccionario_nombre)
    return nombre

    
def numero():
    global valor
    while True:
        diccionario_factorial=[]
        valor = input("Ingrese un número entero: ")
        try:
            valor = int(valor)
            print ('El valor ingresado es :',valor)
            nuevo_valor=valor
            x=valor
            for n in range(valor) :
                nuevo_valor = (x-1)*nuevo_valor
                print (nuevo_valor)
                diccionario_factorial.append(nuevo_valor)
                datos_factorial.append(diccionario_factorial)
                x=x-1
                if x== 2:
                    break
            return valor
        except ValueError:
            print ("Debe ser un número entero.")




def listar_datos():
        for d_c in range(len(datos_nombre)):
            print(datos_nombre [d_c], datos_factorial[d_c])

for c in range(2):
   nombres()
   numero()



listar_datos()

