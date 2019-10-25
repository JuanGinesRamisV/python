#juan gines ramis vivancos p6ej2
#Escribe un programa que te pida números
#y los guarde en una lista. Para terminar de introducir número,simplemente
#escribe “Salir”.El programa termina escribiendo la lista de números.
print('introduce un numero')
numero=int(input())
numeros=[]
numeros.append(numero)
while numero!=('salir'):
    print('introduce otro numero')
    numero=str(input())
    if numero!=('salir'):
       numeros.append(numero) 
print(numeros)
