#juan gines ramis vivancos p5ej12
#di si un numero es primo o no
print('dame un numero')
numero=int(input())
final=0 #final se usa para contabilizar la cantidad de veces que el numero puede ser dividido con resto 0 si final==2 numero es primo
for i in range(numero):
    if((numero)%(i+1)==0):
        final=final+1
    
if(final==2):
    print(numero, 'es primo')
else:
    print(numero, 'no es primo')

primo=True
for i in range(2,numero):
    if numero%i==0:
        primo=False



