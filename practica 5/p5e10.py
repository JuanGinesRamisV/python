#juan gines ramis vivancos p5ej10
#imprime un triangulo
print('altura del triangulo')
altura = int(input())
anchuraini = altura//2
anchura=0
for i in range(altura):
    if (i==0):
        print(' '*anchuraini+'*')
    elif (i>0):
        anchura=anchura+1
        print(' '+'*'*anchura+'*'+'*'*anchura)
    elif(i+1==altura):
        anchura=anchura+1
        print('*'*anchura+'*'+'*'*anchura)
