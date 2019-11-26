#juan gines ramis vivancos p7ej12a
#Escribir un programa que lea una frase, y pase ésta como
#parámetro a una función que debe contar el número de palabras que
#contiene. Debe imprimir el programa principal el resultado.
#Asumir que cada palabra está separada por un solo blanco:

def contador_palabras(frase):
    palabras=1#se supone que siempre hay como minimo una palabra
    palabras+=frase.count(' ',)
    if palabras==1:
        print('hay una palabra en la frase')
    else:
        print('hay',palabras,'palabras en la frase')

frase=str(input('dame una frase: '))
contador_palabras(frase)
