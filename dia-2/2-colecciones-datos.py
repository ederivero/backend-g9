# Listas (tiene la misma funcionabilidad que un arreglo en JS)
# Coleccion de datos ORDENADAS y modificables 

nombre = ['Angel', 'Carmen', 'Sofia', 'Adolfo', 'Henry', 'Felipe']

# las listas pueden contener diferentes tipos de datos
miscelaneo = ['Jueves', 13, 'Soleado', False, [1,2,3]]

# podemos acceder a su contenido mediante las posiciones
print(nombre[0])

# longitud > cantidad de elementos que hay en esa coleccion
# posicion > ubicacion de un elemento determinado, que siempre empieza en 0
# len() > devuelve el numero de items de un contenedor, puede ser un string (y retornara los caracteres) o una coleccion de datos y retornara los items
print(len(nombre))
longitud = len(nombre)
print(nombre[longitud - 1])

# la ultima posicion de la lista
print(nombre[-1])
print(nombre[-2])

# desde la posicion 1 hasta menor que 4
print(nombre[1:4])
# desde la posicion 1 hasta el final
print(nombre[1:])
# desde el inicio hasta menor que 5
print(nombre[:5])
# copiar el contenido de un arreglo (colocandolo en otra posicion de memoria)
print(nombre[:])
print(id(nombre))
alumnos_lima = nombre
print(id(alumnos_lima))
# si cambiamos el contenido de una posicion de memoria, agregamos, o eliminados el contenido se vera reflejado tanto en la variable original como en la variable huesped
nombre[0]= 'Felix'

# si cambiamos el contenido de la variable AHI RECIEN la variable huesped 'alumnos_lima' cambiara su ubicacion en la memoria
nombre = 'hola mundo'
print(alumnos_lima)



print([1,2,3] + [4,5,6])
# en base a la concatenacion y a la sub busqueda de arreglos como podria mostrar sin Sofia (2)
nombre = ['Angel', 'Carmen', 'Sofia', 'Adolfo', 'Henry', 'Felipe', 'Adolfo']

# mostrar solo a Angel y Carmen, luego Mostrar a Adolfo, Henry y Felipe y luego concatenar las dos listas
print(nombre[:2] + nombre[3:])

# agregar un nuevo elemento a la lista
nombre.append('Juan Pablo')

print(nombre)

# eliminar segun el indice
alumno_eliminado = nombre.pop(0)
print(alumno_eliminado)
print(nombre)

# remove(valor) > si no existe el valor emitira un error, si si existe, lo eliminara, no devuelve nada 
alumno_eliminado_2 =nombre.remove('Adolfo')
print(nombre)
print(alumno_eliminado_2)

# del elimina la posicion (muy parecido al pop pero no devuelve nada)
del nombre[0]
print(nombre)

# limpia por completo la lista
nombre.clear()
print(nombre)

# Para mas informacion: https://docs.python.org/3/tutorial/datastructures.html