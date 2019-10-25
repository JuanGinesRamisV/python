#juan gines ramis vivancos
#Escribe un programa que te pida palabras y las guarde en una lista.
#Para terminar de introducir palabras, simplemente pulsa Enter.
#El programa termina escribiendo la lista de palabras.
palabras=[]
print('introduce una palabra')
palabra=str(input())
palabras.append(palabra)
while palabra !='':
    print('introduce otra palabra')
    palabra=str(input())
    palabras.append(palabra)
palabras.remove('')
print(palabras)
