# encapsulamiento > es el metodo de 'ocultar' cierta informacion sensible o que no debe ser manipulada desde fuera de la clase (atributo o metodo privado) 

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        # __atributo > estaremos indicando que sera privado y por ende no puede ser accedido desde fuera de la clase PRIVADO
        self.__ventas = []
        # _atributo > atributo PROTEGIDO en Python mas que todo funciona para cuando queremos utilizar este atributo con herencia
        self._precio_mayorista = 100
    
    def generar_venta(self, fecha, cliente, cantidad):
        # antes de agregar la venta validar si aun tenemos stock para dicha venta
        # TODO: primero ver si tenemos ventas , si hay iteramos esas ventas y sacamos cuanto de cantidad hemos vendido. Luego ver si ese numero es menor que la cantidad total (el atributo cantidad) si es mayor indicar que YA hemos sobregirado las ventas. Por ultimo a esa cantidad de productos vendidos sumar la cantidad entrante y ver si es menor o igual que la cantidad total, si lo es, entonces generar la venta, caso contrario, no permitir la venta e indicar que no hay stock suficiente. Si es que no hay el saldo suficiente indicar cuanto es lo que tenemos para vender (Hasta el proximo miercoles 26)
        venta = {
            'fecha': fecha,
            'cliente': cliente,
            'cantidad': cantidad
        }
        self.__ventas.append(venta)
        print(self.__sacar_igv(self.precio))
        print('Venta registrada exitosamente')
    
    def mostrar_ventas(self):
        # retornar las ventas registradas de ese producto
        return self.__ventas
    
    def __sacar_igv(self, precio):
        # Este metodo pasa a ser privado desde que le ponemos '__' al inicio del nombre
        print(precio * 0.18)
        return (precio * 1.18) - precio



detergente = Producto(nombre='Detergente Sapito', precio=4.50, cantidad=50)
detergente.nombre = 'Detergente Lechuga'
print(detergente.nombre)

detergente.generar_venta(fecha='2022-10-19', cliente='Eduardo de Rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='Julissa Perez', cantidad=30)
detergente.generar_venta(fecha='2022-10-30', cliente='Franco Portugal', cantidad=20)
detergente.generar_venta(fecha='2022-11-02', cliente='Michelle Ordoñez', cantidad=15)
# print(detergente.__ventas)

print(detergente.mostrar_ventas())


# No se puede acceder al metodo __sacar_igv desde que es un metodo privado
# print(detergente.__sacar_igv(80.00))
