#juan gines ramis vivancos p6ej7
#Escribe un programa que pida un número (límite) y luego te pida
#números hasta que la suma de los números introducidos supere el límite inicial.
numeros=[]
suma=0
print('escribe limite')
limite=int(input())
print('escribe un valor')
numero=int(input())
numeros.append(numero)
suma=suma+numeros[-1]
while suma<limite:
    print('escribe otro valor')
    numero=int(input())
    numeros.append(numero)
    suma=suma+numeros[-1]
print('El limite a superar es',limite,'. La lista creada es: ',end='')
for i in range(len(numeros)):
    if i==(len(numeros)-1):
        print(numeros[-1], end='')
    else:
        print(numeros[i],',',end='')
print(' ya que la suma de estos valores es', suma,end='')
    
