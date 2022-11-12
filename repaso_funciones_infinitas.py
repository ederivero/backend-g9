def prueba(**argumentos):
    print(argumentos)


prueba(nombre='eduardo', apellido='de rivero')

persona = {
    'nombre':'eduardo',
    'apellido': 'de rivero'
}

prueba(persona=persona)

# Cuando nosotros en una funcion pasamos un DICCIONARIO pero con doble asterisco antes (**) significa que sacara las llaves (keys) y lo colocara como parametro de la funcion y sus valores como los valores de esos parametros
prueba(**persona)
prueba(nombre= persona['nombre'], apellido=persona['apellido'])

# si usamos una funcion con parametros definidos entonces tenemos que indicar en el diccionario ESE MISMO NOMBRE DE PARAMETROS ya que si es diferente, arrojara un error
def saludar(nombre, apellido):
    print(nombre, apellido)


usuario = {
    'nombre': 'eduardo',
    'apellido': 'derivero'
}
usuario2= {
    'nombrecito': 'juanito'
}

saludar(**usuario)
# Esto me arrojara un error ya que el parametro 'nombrecito' no concuerda con el parametro esperado (nombre)
saludar(**usuario2)
saludar(nombrecito='pedrito')