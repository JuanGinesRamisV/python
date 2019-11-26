#juan gines ramis vivancos
#Escribe un programa que lea una frase, y la pase como parámetro a un
#procedimiento, y éste debe mostrar la frase con un carácter en cada línea.
frase=input('introduce una frase: ')
def proce(frase):
    for i in range(len(frase)):
        print(frase[i])
proce(frase)
