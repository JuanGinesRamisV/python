#juan gines ramis p4ej1
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
if n1<n2:
    ngrande = n2
    npequeño = n1
else:
    ngrande = n1
    npequeño = n2
if ngrande<n3:
    ngrande = n3
if ngrande<n4:
    ngrande = n4
if ngrande<n5:
    ngrande = n5
print('el numero mayor es' ,ngrande,)

if npequeño>n3:
    npequeño = n3
if npequeño>n4:
    npequeño = n4
if npequeño>n5:
    npequeño = n5
print ('el numero peuqeño es' ,npequeño,)
