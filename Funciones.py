import os
os.system('cls')

nombre =""
#diccionario_nombre=[]
#diccionario_factorial = []
datos_nombre=[]
datos_factorial =[]
s=""

while s!='salir':
    diccionario_nombre=[]
    diccionario_factorial = []
    def nombres():
        nombre = input ("Ingresar Nombre    ")
        print ('nombre : ',nombre)
        diccionario_nombre.append(nombre)
    def numero():
        global valor
        while True:
            valor = input("Ingrese un número entero: ")
            try:
                valor = int(valor)
                return valor
            except ValueError:
                print ("Debe ser un número entero.")
    nombres()
    numero()
    print ('El valor ingresado es :',valor)
    nuevo_valor=valor
    x=valor
    for n in range(valor) :
        nuevo_valor = (x-1)*nuevo_valor
        print (nuevo_valor)
        diccionario_factorial.append(nuevo_valor)
        x=x-1
        if x== 2 :
            break
    datos_nombre.append(diccionario_nombre)
    datos_factorial.append(diccionario_factorial)
    s=input('Otro Nombre (salir=Finalizar   :')


print()

print()
for d_c in range(len(datos_nombre)):
    print(datos_nombre [d_c], datos_factorial[d_c])

