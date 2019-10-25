#juan gines ramis vivancos p5e4
#Escribe un programa que pida un número y calcule su factorial.
print('dame un numero')
numero = int(input())
por = 1
for i in range(numero):
    por = por*(i+1)
print('El factorial de',numero, 'es',por,)
