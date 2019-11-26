#Escribe un programa que lea el nombre de una persona y un carácter, le pase estos
#  datos a una función que comprobará si dicho carácter está en su nombre. 
# El resultado de dicha función lo imprimirá el programa principal por pantalla.
def contar(nombre,carater):
    if carater in nombre:
        return(caracter, 'esta en tu nombre')
    else:
        return(caracter, 'no esta en tu nombre')

nombre=str(input('dime tu nombre'))
caracter=str(input('dime un caracter'))
print(contar(nombre,caracter))
