#juan gines ramis vivancos p5ej11
#Escribe un programa que pida un número e imprima todos sus divisores.
print('dame un numero')
numero=int(input())
for i in range(numero):
    if(numero%(i+1)==0):
        print(i+1)
