print('introduce el dia')
dia = int(input())
print('introduce el mes')
mes = int(input())
print('introduce el año')
año = int(input())

if año>=0:
    if 0<mes<=12:
        if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if 0<dia<=31:
                print('fecha correcta')
            else:
                print('fecha incorrecta')
        elif mes == 4 or 6 or 9 or 11:
            if 0<dia<=30:
                print('fecha correcta')
            else:
                print('fecha incorrecta')
        elif mes == 2:
            if 0<dia<=29:
                print('fecha correcta')
            else:
                print('fecha incorrecta')

    else:
        print('fecha incorrecta')
else:
        print('fecha incorrecta')
