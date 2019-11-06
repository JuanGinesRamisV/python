#juan gines ramis vivancos
#Escribir un programa para jugar a adivinar un número
#(el ordenador "piensa" el número y el usuario lo ha de adivinar).
#El programa empieza pidiendo entre qué números está el número a adivinar,
#se "inventa" un número al azar y luego el usuario va probando valores.
#El programa va decidiendo si son demasiado grandes o pequeños. pista:
import random
import time
intentos=[]
random.seed (time.time ())
minimo = int (input ( "Valor mínimo:"))
maximo = int (input ( "Valor máximo:"))
secreto = random.randint (minimo, maximo)
numero=()
while numero != secreto:
    numero = int(input("introduce un número"))
    intentos.append(numero)
print ("lo has conseguido. Lo has intentado", len(intentos),)
    
