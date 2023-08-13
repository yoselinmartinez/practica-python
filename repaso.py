# Hacer una funcion que reciba un nombre e imprima un saludo 
# ej. Hola Jorge !
#ej. Hola Beto !


# def saludo (nombre):
#     print("Hola " + nombre )

# saludo("Jorge")
# saludo("Beto ")
# saludo('perro')

#Hacer una funcion que reciba 2 numeros e imprima la suma de los numeros

# def suma (num1, num2):
#     resultado  = num1 + num2
#     print('El reultado de sumar ' +str(num1)+ ' y '+ str(num2)+ ' es '+ str(resultado))

# suma(1024, 518)
# suma(71,397)

#Hacer una funcion que reciba una lista e imprmia todos los elemetos
# frutas = ['Bananna','Mango','Fresa','Guayaba']
# coches = ['BMW','Mercedes','Audi']
# animales = ['Orca','Elefante','Ardilla']

# def imprimir_lista (lista):
#     for cosa in lista:
#         print(cosa)


# imprimir_lista(frutas)
# imprimir_lista(coches)
# imprimir_lista(animales)

#Hacer una funcion que reciba un diccionario de paises y capitales y los imprima de la siguiente forma
# La capital de USA es Washington
# La capital de Mexico es CDMX
# La capital de Argentina es Buenos Aires

# paises_y_capitales = {'USA':'Washington',
#                       'Mexico':'CDMX',
#                       'Argentina':'Buenos Aires'
#                       }

# def imprimir_paises_y_capitales (diccionario):
#     for pais in diccionario.keys():
#         capital = paises_y_capitales[pais]
#         print('La capital de ' + pais + ' es ' + capital )

# imprimir_paises_y_capitales(paises_y_capitales)



#Dado un diccionario con las calificaciones de cada alumno, imprimir la calificacion de cada alumno
#ej Jorge saco 10
#ej Carlos saco 8
#ej Ximena saco 9
#ej America saco NP

calificaciones_3roB = {'Jorge':10,'Carlos': 8,'Ximena': 9, 'America': 'NP'}

def imprimir_califcaciones(diccionario):
    for alumno in diccionario.keys():
        calificacion = diccionario[alumno]
        print(alumno+ ' saco ' + str(calificacion) )

imprimir_califcaciones(calificaciones_3roB)










