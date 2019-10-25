#juan gines ramis vivancos
#Escribe un programa que te pida dos números,
#de manera que el segundo sea mayor que el primero.El programa termina
#escribiendo los dos números tal y como se pide:
print('introduce un numero')
numero=int(input())
numeros=[]
numeros.append(numero)
print('introduce un numero mayor que', numero)
numero=int(input())
numeros.append(numero)
while numeros[0]>=numeros[1]:
    print(numeros[0], 'no es mayor que',numeros[1],'. introduce otro numero')
    numero=int(input())
    numeros[1]=numero
print('los numeros que has escrito son',numeros[0], 'y', numeros[1])

    
