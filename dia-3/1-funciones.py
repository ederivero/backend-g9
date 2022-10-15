# Funciones definidas por el usuario
def miFuncion():
  print('Hola mundo')

def suma(a, b):
  return a + b

def comprobarEdad(edad):
  if (edad >= 18):
    return 'Eres mayor de edad'
  else:
    return 'No eres mayor de edad, no puedes ingresar'

# edad = input('Ingrese su edad: ')
# edad = int(edad)
# print(comprobarEdad(edad))

alumnos = ['Eduardo', 'Pepe', 'Jose', 'Miguel', 'Julia', 'Raul']

def buscarNombre():
  if not 'Eduardo' in alumnos:
    return False
  # else:
  #   return True
  return True



todos_lo_nombres = input('Ingrese nombres separados por comas: ')

nombre_a_buscar = input('Ingrese el nombre a buscar: ')

def separarNombres(lista_nombres):
  nombres = lista_nombres.split(',')
  return nombres


def buscarPersona(nombre):
  array_nombres = separarNombres(todos_lo_nombres)

  if nombre in array_nombres:
    return '{} ha sido encontrado {}'.format(nombre, '😃')
  return f'No pudimos encontrar a {nombre} {"😢"}'

print(buscarPersona(nombre_a_buscar))
