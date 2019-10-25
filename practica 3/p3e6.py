#juan gines ramis vivancos p3e6
#Pida al usuario el precio de un producto y el nombre del producto y muestre
#el mensaje con el precio del IVA (21%). Por ejemplo:
#“ Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en
#total”.
print('introduce el precio del producto')
precio=float(input())
print('introduce el nombre del producto')
producto=str(input())
preciofinal=precio*1.21
print('tu',producto,'vale',precio,'euros y con el 21% de IVA se queda en',
      preciofinal,'euros en total')
