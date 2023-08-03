'''#Con un ciclo for, imprime los nombres de la lista
nombres = ['Jorge', 'Victor' , 'Carlos']

for nombre in nombres:
    print(nombre)

#Con un ciclo for, imprime los valores del diccionario
datos = {
	'nombre' : 'manchis',
	'edad' : '2 anios',
	'peso' : '2kg',
	'color' : 'combinadito'
}

for llave in datos.keys():
    valor = datos[llave]
    print(valor)

#Si el valor de edad es igual a 18, imprime 'Es mayor de edad!'
edad = 27
if edad == 18:
    print('Es mayor de edad')

#Con un ciclo for, imprime el numero SOLO si el numero es igual a 5
mis_numeros = [2,3,1,7,5,3,5,7,5,8,3,7,3,5]

for numero in mis_numeros:
    if numero == 5:
        print(numero)

#Con un ciclo for, imprimer el numero de veces que 'Jorge' sale en
#la lista
alumnos = ['Andrea', 'Ximena', 'Jorge', 'Roberto', 'Victor', 'Jorge']
i = 0 
for nombre in alumnos:
    if nombre == 'Jorge':
        i += 1
print(i)

#Con un ciclo for, imprimir el numero de veces que el 8 sale en la lista,
#El mensaje que se imprima, debe decir: El ocho aparecio x veces
lista = [1,3,6,2,5,7,8,2,1,3,8,4,5,3,8,9,3,1]
i = 0
for numero in lista:
    if numero == 8:
        i += 1
print('El ocho aparecio ' + str(i) +' veces')

#Con un ciclo while imprimir los numeros del 0 al 100

i = 0
while i <= 100:
    print(i)
    i += 1

#Imprime el tercer elemento de la lista
frutas = ['Cereza','Melon','Guayaba','Mango','Sandia']
print(frutas[2])'''

#Con un ciclo while, imprimir los valores de la lista
paises_que_han_ganado_un_mundial = ['Argentina','Francia','Alemania','Brazil','Espania','Uruguay']

i = 0

while i <= 5 :
    print (paises_que_han_ganado_un_mundial[i])
    i += 1





