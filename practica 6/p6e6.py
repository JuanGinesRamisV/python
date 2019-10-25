#juan gines ramis vivancos p6ej6
#Escribe un programa que pida primero dos números (máximo y mínimo) y
#que después te pida números intermedios.
numeros=[]
print('escribe un numero')
numero1=int(input()) #numero pequeño
print('escribe otro numero')
numero2=int(input()) #numero grande
while numero1>numero2:
    print(numero2, 'no es mayor que',numero1,'vuelve a probar')
    numero2=int(input())
print('escribe un numero entre',numero1,'y',numero2)
numero3=int(input())#numero intermedio
if numero1<numero3<numero2:
    while numero1<numero3<numero2:
        numeros.append(numero3)
        print('esribe un numero entre',numero1,'y',numero2,)
        numero3=int(input())
    print('Los numeros situados entre',numero1,'y',numero2,'que has escrito son')
    for i in range(len(numeros)):
        if i==(len(numeros)-1):
            print(numeros[-1],end='')
        else:
            print(numeros[i],',', end='')
else:
    print(numero3,'no esta entre',numero1, 'y',numero2)
    
