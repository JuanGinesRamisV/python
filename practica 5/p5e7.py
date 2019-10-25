#juan gines ramis vivancos p5e7
#Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera
print('introduce la altura de tu trianuglo')
altura = int(input())
anchura = altura
for i in range(altura+1):
    print('*'*(altura-(i*1)))
        
