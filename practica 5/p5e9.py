#juan gines ramis vivancos p5e9
#programa que te imprime un rectangulo
print('anchura del rectángulo')
anchura = int(input())
print('altura del rectángulo')
altura = int(input())
for i in range(altura):
    if i==0:
        print('*'*anchura)
    elif 0<i<altura-1:
        print('*'+(anchura-2)*' '+'*')
    elif i+1==altura:
        print('*'*anchura)
    
