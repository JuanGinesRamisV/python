#juan gines ramis vivancos
#Escribe un programa que te pida una frase y una vocal, y pase estos datos
#como parámetro a una función que se encargará de cambiar todas las vocales
#de la frase por la vocal seleccionada. Devolverá la función la frase
#modificada, y el programa principal la imprimirá:

def cambio(frase,vocal):
    vocales=['a','e','i','o','u']
    if vocal in vocales:
        for i in range(len(vocales)):
            frase=frase.replace(vocales[i],vocal)
        return(frase)
    else:
        return(vocal,'no es una vocal')

frase=str(input('introduce una frase: '))
vocal=str(input('introduce una vocal: '))
print(cambio(frase,vocal))
