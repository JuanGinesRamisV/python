#juan gines ramis vivancos P4ej2
#Pida al usuario 5 números y diga cual es el mayor y cuál el menor.
print('introduce el primer numero')
n1 = float(input())
print('introduce el segundo numero')
n2 = float(input())
print('introduce el tercer numero')
n3 = float(input())
print('introduce el cuarto numero')
n4 = float(input())
print('introduce el quinto numero')
n5 = float(input())
if n1<n2<n3<n4<n5:
    print('los numeros estan en ordes ascendente')
elif n1>n2>n3>n4>n5:
    print('los numeroes estan en orden descendente')
else:
    print('los numeros no estan ordenados')
    
