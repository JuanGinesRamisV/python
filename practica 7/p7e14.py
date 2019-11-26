def dias():
    mesese={1: "enero",
            2: "febrero",
            3: "marzo",
            4: "abril",
            5: "mayo",
            6: "junio",
            7: "juliio",
            8: "agosto",
            9: "setiembre",
            10: "octubre",
            11: "noviembre",
            12: "diciembre"}
    dia=int(input("introduce un dia: "))
    mes=int(input("introduce un mes: "))
    año=int(input("introduce un año: "))
    print(dia,' de',mesese[mes],'de ',año)

dias()
