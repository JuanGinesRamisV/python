#juan gines ramis vivancos p6ej3
#Escribe un programa que pida notas y los guarde en una lista.
#Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
#El programa termina escribiendo la lista de notas.
print('introduce la primera nota')
nota=float(input())
notas=[]
notas.append(nota)
while 0<=nota<=10:
    print('introduce otra nota')
    nota=float(input())
    notas.append(nota)
notas.remove(nota)
print(notas)

