#juan gines ramis vivancos p7ej10
#Escribe un programa que te pida una palabra o número,
#pase por parámetro estos datos a una función, y ésta te diga si
#es o no palíndroma o capicúa. El programa principal imprimirá el
#resultado de la función:

def palindromo(palabra):
    contador=0
    longitud=len(palabra)
    for i in range(len(palabra)):
        if i==0:
            if(palabra[i]==palabra[-1]):
                contador+=1
        else:
            if(palabra[i]==palabra[-i-1]):
                contador+=1        
    if (contador==len(palabra)):
        print('es un palindromo')
    else:
        print('no es un palindromo')


palabra=str(input('dame una palabra: '))
palindromo(palabra)
        
    
