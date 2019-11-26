#juan gines ramis vivancos
#Escribe un programa que le
#pida al usuario si quiere calcular si un número es primo con for o con while
def primo_while(numero):
    primo=0 #se utiliza para contabilizar si el numero es primo o no
    divisor=(1)
    while (primo<2):
        if ((numero%divisor)==0):
            primo+=1
        if divisor!=numero:
            divisor+=1
        
    if numero==divisor:
        return('tu numero es primo')
    else:
        return('tu numero no es primo')

def primo_for(numero):
    final=0 #final se usa para contabilizar la cantidad de veces que el numero puede ser dividido con resto 0 si final==2 numero es primo
    for i in range(numero):
        if((numero)%(i+1)==0):
            final=final+1
    
    if(final==2):
        return(numero, 'es un numero primo')
    else:
        return(numero, 'no es primo')

numero=int(input('dame un numero'))
print('1) primo con while')
print('2) primo con for')
menu=int(input('dame una opción'))
if (menu==1):
    print(primo_while(numero))
else:
    print(primo_for(numero))
