#juan gines ramis vivancos p6ej9
#Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S”
usuario=[]
usuarios=[]
print('introduce tu nombre de usuario')
nombre=str(input())
print('introduce tu numero de telefono')
telefono=int(input())
while nombre !='s':
    usuario+=[nombre, telefono]
    usuarios+=[usuario]
    usuario=[]
    print('introduce tu nombre de usuario')
    nombre=str(input())
    print('introduce tu numero de telefono')
    telefono=int(input())
for i in range(len(usuarios)):
    print(usuarios[i][0], end=': ')
    print(usuarios[i][1])
    
