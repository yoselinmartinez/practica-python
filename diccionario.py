#esta entre {}
#tiene una llave y un valor 
#las llaves no se pueden repedir
#los valores estan asignado a sus llaves por :
#las llaves son unicas y no editables 
#pueden ser anidados

#crear un diccionario con la materia y calificacion de ultimo semestre 
'''calificaciones = {'embebidos': 10, 'admin_redes':9,'lab_admin':10}

print(calificaciones['admin_redes'])'''

#crear un diccionario con las comidas que me gustan y que no me gustan 

comidas = {'me_gustan': ['papas','hamburguesa'],'no_me_gustan':['mole','moronga']}

print(comidas['me_gustan'])

#agregar elemento a la lista 
comidas['me_gustan'].append('carne')

print(comidas['me_gustan'])

#agregar una nueva llave, valor al diccionario 
comidas.update({'comidas_equis':['crema','chilaquiles','enchiladas']})

print(comidas)

#de las comidas equis, imprimir la segunda 
print(comidas['comidas_equis'][1])


