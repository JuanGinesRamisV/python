#juan gines ramis vivancos
#Escribe un programa que lea el nombre y los dos apellidos de una persona
#(en tres cadenas de caracteres diferentes), los pase como parámetros a una
#función, y ésta debe unirlos y devolver una única cadena. La cadena final
#la imprimirá el programa por pantalla.
def nom(nombre,apellido,apellido1):
    nombre=nombre.replace(' ','')#Por si el usuario tiene nombre compuesto
    print(nombre+apellido+apellido1)
    
nombre=str(input('introduce tu nombre: '))
apellido=str(input('introduce tu apellido: '))
apellido1=str(input('introduce tu segundo apellido '))
nom(nombre,apellido,apellido1)

    
