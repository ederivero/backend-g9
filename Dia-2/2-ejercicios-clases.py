# Crear una clase llamada Persona en la cual se guarden: nombre, fecha_nacimiento, nacionalidad y dni. Crear otra clase llamada Alumno que va a heredar la clase Persona y ademas va a tener sus atributos: num_seguro, num_emergencia, matriculado (Boolean), el alumno tendra un metodo llamado mostrar_datos y ademas otro metodo llamado matricular en el cual si esta matriculado no se podra matricular, caso contrario, si. Y tambien tener otra clase Profesor que va a tener cta_pago y maestria (str) y el profesor puede mostrar su cta_pago y ademas si tiene maestria al momento de mostrar la cta_pago indicar que se le tiene que agregar 100 soles
class Persona:
    def __init__(self, nombre, fec_nac, dni, nacionalidad):
        self.nombre = nombre
        self.fec_nac = fec_nac
        self.nacionalidad = nacionalidad
        self.dni = dni

    def saludar(self):
        print("Hola, me llamo {}".format(self.nombre))


class Alumno(Persona):
    def __init__(self, nombre, fec_nac, dni, nacionalidad, num_seguro, num_emergencia, matriculado):
        super().__init__(nombre, fec_nac, dni, nacionalidad)
        self.num_seguro = num_seguro
        self.num_emergencia = num_emergencia
        self.matriculado = matriculado

    def mostrar_datos(self):
        return {
            'nombre': self.nombre,
            'fec_nac': self.fec_nac,
            'dni': self.dni,
            'nacionalidad': self.nacionalidad,
            'num_seguro': self.num_seguro,
            'num_emergencia': self.num_emergencia,
            'matriculado': self.matriculado
        }

    def matricular(self):
        if self.matriculado:
            return 'No se puede'
        else:
            return 'Matriculado correctamente'


class Profesor(Persona):
    def __init__(self, nombre, fec_nac, dni, nacionalidad, cta_pago, maestria):
        super().__init__(nombre, fec_nac, dni, nacionalidad)
        self.cta_pago = cta_pago
        self.maestria = maestria

    def mostrar_cta(self):
        if self.maestria:
            return {
                'cta_pago': self.cta_pago,
                'nota': 'Se le tiene que agregar 100 soles'
            }
        else:
            return {
                'cta_pago': self.cta_pago,
            }
