#juan gines ramis vivancos
#Escribe un programa que te pida los nombres y notas de alumnos.
#Si escribes una nota fuera del intervalo de 0 a 10, el programa
#entenderá que no quieres introducir más notas de este alumno.
#Si no escribes el nombre, el programa entenderá que no quieres introducir
#más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene
#esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc],
#[nom3, nota1, nota2, etc], etc]
alumnos=[]
print('introduce el nombre del alumno')
nombre=str(input())
while nombre!='':
    alumno=[]
    alumno+=[nombre]
    nota=float(input("Introduce la nota del alumno: "))
    while 0<=nota<=10:
        alumno+=[nota]
        nota=float(input('introduce la nota sel alumno: '))
    alumnos+=[alumno]
    print('introduce otro nombre')
    nombre=str(input())
for i in range(len(alumnos)):
    for j in range(len(alumnos[i])):
        if j == 0:
            print(alumnos[i][j], end=': ')
        elif j < ((len(alumnos[i])-1)):
            print(alumnos[i][j], end=' - ')
        else:
            print(alumnos[i][j])
                
            
        
        
        
               
    
        
    
