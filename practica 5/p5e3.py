#juan gines ramis vivancos p5e3
#Escribe un programa que pida dos números y escriba la suma de
#enteros desde el primero hasta el último.
print('dame un número')
numero1 = int(input())
print('dame un número mayor que',numero1,)
numero2 = int(input())
suma = 0
for i in range(numero1,numero2+1):
              suma = suma+i
print(suma)
              

