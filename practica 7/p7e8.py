#juan gines ramis vivancos p7ej8
#Escribe un programa que pida una frase, y pase la frase como
#parámetro a una función que debe eliminar los espacios en blanco #
#compactar la frase).El programa principal imprimirá
#por pantalla el resultado final

def no_espacio(frase):
    frase=frase.replace(' ','')
    return(frase)

a=str(input('dime una frase: '))
print(no_espacio(a))
