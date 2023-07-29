def saludar():
    print("Holi crayoli")

saludar()

#hacer una funcion que reciba un nombre e imprima un saludo con el nombre 

def saludar_con_nombre(nombre_de_persona):
    print("Holi " + nombre_de_persona)

saludar_con_nombre("Yoselin")

#crear una funcion que reciba una lista con la inf personal 
#e imprima si puede o no trabajar en liverpool

def puede_trabajar_liverpool(lista):
    edad = lista[0]
    estudia = lista[1]
    if edad >= 18 and estudia == 'estudiante':
        print("Puede trabajar en liverpool")

    else:
        print("No puede trabajar para liverpool")


puede_trabajar_liverpool([19, 'estudiante'])
puede_trabajar_liverpool([19, 'no_estudiante'])
puede_trabajar_liverpool([28, 'no_estudiante'])
puede_trabajar_liverpool([0, 'estudiante']    )
puede_trabajar_liverpool([0, 'estudiante']    )
puede_trabajar_liverpool([17, 'estudiante']   )
puede_trabajar_liverpool([22, 'no_estudiante'])
puede_trabajar_liverpool([24, 'no_estudiante'])
puede_trabajar_liverpool([19, 'no_estudiante'])
puede_trabajar_liverpool([25, 'no_estudiante'])
puede_trabajar_liverpool([25, 'estudiante'])
puede_trabajar_liverpool([24, 'no_estudiante'])
puede_trabajar_liverpool([14, 'estudiante'])
puede_trabajar_liverpool([17, 'no_estudiante'])
puede_trabajar_liverpool([26, 'no_estudiante'])       

