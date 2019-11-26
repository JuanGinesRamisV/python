#juan gines ramis vivancos
#Escribe un programa que pida dos palabras las pase
#como parámetro a un procedimiento y diga si riman o no.
#Si coinciden las tres últimas letras tiene que decir que riman.
#Si coincidensólo las dos últimas tiene que decir que riman un poco
#y si no, que no riman.

def rima(palabra1,palabra2):
    contador=0
    for i in range(3,0,-1):
        if palabra1[i]==palabra2[i]:
            contador+=1
    if contador==3:
        return('las palabras riman mucho')
    elif contador==2:
        return('las palabras riman un poco')
    else:
        return('las palabras no riman mucho')


palabra1=str(input('dame una palabra 1: '))
palabra2=str(input('dame una palabra 2: '))
print(rima(palabra1,palabra2))
