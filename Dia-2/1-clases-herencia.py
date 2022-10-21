# herencia > sirve para reutilizar una clase previamente definida

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    
    def mostrar_resumen(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo
        }

class Alumno(Usuario):
    def __init__(self, correo, apellido, nombre, telefono_emergencia):
        self.telefono_emergencia = telefono_emergencia
        super().__init__(nombre, apellido, correo)

    def saludar(self):
        print('hola yo soy la clase alumno y el nombre es {}'.format(self.nombre))
    
    def mostrar_resumen(self):
        # Polimorfismo > Poli > muchas | morfa > formas muchas formas o muchos significados la forma en la cual un metodo dependendiendo de donde se utilice va a trabajar de una manera u otra
        resumen = super().mostrar_resumen()
        resumen['telefono_emergencia'] = self.telefono_emergencia
        return resumen

usuario01 = Usuario(nombre='Eduardo', apellido='De Rivero', correo='ederiveroman@gmail.com')
usuario02 = Usuario('Alejandra','Perez','aperez@gmail.com')
usuario03 = Usuario(correo='jdias@hotmail.com', apellido='Dias', nombre='Javier')

print(usuario01.mostrar_resumen())


alumno01 = Alumno('jmartinez@yahoo.es', 'Martinez', 'Juan', '974207075')
alumno01.saludar()
print(alumno01.mostrar_resumen())