#juan gines rammis vivvancos p4e4
#Pida al usuario tres números y un cuarto número,
#y compruebe si éste último es divisor de los tres números primeros.
print('introduce 3 numeros')
n1 = int(input())
n2 = int(input())
n3 = int(input())
print('introduce un numero y comprobare si es divisor de los 3 primeros')
n4 = int(input())
if n1%n4 == 0:
    print(n4, 'es divisor de' ,n1,)
    if (n2%n4 == 0):
        print(n4, 'es divisor de' ,n2,)
        if(n3%n4 == 0):
            print(n4, 'es divisor de' ,n3,)
        else: print(n4 ,'no es divisor de' ,n3,)
    else:
        print(n4, 'no es divisor de' ,n2,)
        if (n3%n4 == 0):
            print(n4, 'es divisor de' ,n3,)
        else:
            print(n4, 'no es divisor de' ,n3,)

else:
    print(n4, ' no es divisor de' ,n1,)
    if (n2%n4 == 0):
        print(n4, 'es divisor de' ,n2,)
        if(n3%n4 == 0):
            print(n4, 'es divisor de' ,n3,)
        else: print(n4 ,'no es divisor de' ,n3,)
    elif(n2%n4 != 0):
        print(n4, 'no es divisor de' ,n2,)
        if(n3%n4 ==0):
            print(n4, 'es divisor de',n3,)
        else:
            print(n4, 'no es divisor de',n3)
    
