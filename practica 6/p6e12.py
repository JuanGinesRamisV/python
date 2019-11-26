
#juan gines ramis vivancos
#Escribir un programa para jugar a adivinar un número (el usuario piensa
#un número y el programa lo ha de adivinar). El programa empieza pidiendo
#entre qué números está el número a adivinar y luego intenta adivinar de
#qué número se trata. El usuario va diciendo si el número que ha dicho
#el programa es menor, mayor o igual al que se ha buscado.
import random
import time
intentos=[]
random.seed (time.time ())
minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))
respuesta=str()
while minimo > maximo: #se verifica si los valores se han introducido correctamente
    print(minimo, 'es mayor que', maximo, 'vuelve a introducir los numeros')
    minimo = int (input ( "Valor mínimo:"))
    maximo = int (input ( "Valor máximo:"))
print('piensa un numero entre',minimo, 'y', maximo,'a ver si lo puedo adivinar')
while respuesta != ('igual'):
        secreto = random.randint (minimo, maximo)
        print('dime si' ,secreto, 'es mayor, menor o igual al numero que has pensado')
        respuesta=str(input("Respuesta:"))
        if (respuesta == ('mayor')):
            maximo = secreto
        elif (respuesta == ('menor')):
            minimo = secreto
        elif (respuesta == ('igual')):
            print('gracias por jugar')

                  
    
