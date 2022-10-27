# TODO: Replicar la funcionabilidad de la libreria CamelCase
# HINT: los strings en python son considerados listas
# texto= 'eduardo' > texto[0] = 'e'....
texto = 'hola como estan'


class CamelCasePropia:
    def __init__(self):
        pass

    def hump(self, texto):
        nuevoTexto = texto.split(' ')
        palabrasMayus = []

        for palabra in nuevoTexto:
            palabrasMayus.append(palabra.capitalize())
        nuevoTextoMayus = ' '.join(palabrasMayus)
        return nuevoTextoMayus


cc = CamelCasePropia()
print(cc.hump(texto))
