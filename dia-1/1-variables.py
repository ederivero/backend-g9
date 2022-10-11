# Esto es un comentario
edad = 30

nombre = 'Eduardo'
apellido = "De Rivero"

# No se puede utilizar los backtips (comillas invertidas) para los string
# saludo = `Hola como estan mi nombre es ${nombre}`
mensaje = '''El dia de hoy
empezo el modulo de 
backend'''

despedida = """El dia de hoy
nos despedimos hasta una nueva
oportunidad"""

lastName = "O'neil"
print(type(lastName))

print(nombre)

# En python no hay ni null ni undefined ni NaN (Not A Number) todo ello se resume en None 
especialidad = None 
print(especialidad)

# No hay validaciones al momento de cambiar el tipo de dato
lastName = 80
print(type(lastName))
lastName = None
print(type(lastName))

# type(var) > devolver que tipo de dato es esa variable
print(type(nombre))
print(type(edad))


# tambien se puede declarar varias variables en una misma linea
curso, grupo, mes, dia, nota = 'CodiGo', 'Backend', 'Octubre', 10, 15.4

print(grupo)

# id(var) > mostrar la posicion de memoria en la cual se esta alojando la variable, funcion, clase, etc
print(id(curso))

# del > eliminar la variable (libera la memoria), no se puede volver a utilizar esa variable nunca mas
del curso

print(curso)