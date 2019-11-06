#juan gines ramis vivancos
#Desarrolla de nuevo el ejercicio de la práctica anterior de los números
#primos, con while. Reflexiona y escribe en el propio programa en forma de
#comentario, qué opción es mejor y por qué.
primo=0 #se utiliza para contabilizar si el numero es primo o no
numero=int(input('introduce un numero'))
divisor=(1)
while (primo<2):
    if ((numero%divisor)==0):
        primo+=1
    if divisor!=numero:
        divisor+=1
if numero==divisor:
    print('tu numero es primo')
else:
    print('tu numero no es primo')


    
