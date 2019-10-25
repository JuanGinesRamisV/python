#Juan gines ramis vivancos p4e3
#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.
print('Si quieres calcular el area de un triangulo pon t si la quieres de un'
      'cuadrado pon c')
ans = str(input())
if (ans == 't'):
    print('introduce la base de tu triangulo')
    base = float(input())
    print('introduce la altura de tu traingulo')
    altura = float(input())
    area = (base*altura)/2
    print('el area de tu traingulo es' ,area,)
elif (ans == 'c'):
    print('introduce la base de tu a')
    lado = float(input())
    area = (lado*lado)
    print('el area de tu traingulo es' ,area,)
else:
    print('no se lo que me pides')
    
