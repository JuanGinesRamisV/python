#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento.
#El procedimiento contará el número de vocales (de cada una) que aparecen,
#y lo imprimirá por pantalla.

def contar_vocal(frase):
    vocales=['a','e','i','o','u']
    contador=[0,0,0,0,0]
    for i in range(len(vocales)):
        for j in range(len(frase)):
            if frase[j]==vocales[i]:
                contador[i]+=1
    print('hay',contador[0],'a')
    print('hay',contador[1],'e')
    print('hay',contador[2],'i')
    print('hay',contador[3],'o')
    print('hay',contador[4],'u') 


frase=str(input('dame una frase: '))
contar_vocal(frase)
