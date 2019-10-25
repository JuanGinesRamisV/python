#juan gines ramis vivancos p6ej8
#Escribe un programa que te pida primero un número y
#luego te pida números hasta que la suma de los números
#introducidos coincida con el número inicial.
#El programa termina escribiendo la lista de números.
print('escribe un limite')
limite=int(input())
suma=0
print('escribe un valor')
numero=int(input())
numeros=[]
numeros.append(numero)
suma=suma+numeros[-1]
while suma!=limite:
    if suma>limite:
        print(numeros[-1],'es demasiado grande.',end='')
        suma=suma-numeros[-1]
        del numeros[-1]
    elif suma<limite:
        print('Escribre otro valor')
        numero=int(input())
        numeros.append(numero)
        suma=suma+numeros[-1]
print('el limite a alcanzar es',limite,'.La lista creada es ', end='')
for i in range(len(numeros)):
    if i==(len(numeros)-1):
        print(numeros[i],end='')
    else:
        print(numeros[i],',', end='')

    
