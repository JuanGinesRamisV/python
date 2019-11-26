#juan gines ramis vivancos
#Escribe un programa que pida un texto por pantalla, este texto lo pase
#como parámetro a un procedimiento, y éste lo imprima primero todo en
#minúsculas y luego todo en mayúsculas.
texto=str(input('introduce tu texto: '))
def imprimir(texto):
    print(texto.lower())
    print(texto.upper())

imprimir(texto)
