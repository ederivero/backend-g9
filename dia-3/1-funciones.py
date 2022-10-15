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

print(buscarNombre())