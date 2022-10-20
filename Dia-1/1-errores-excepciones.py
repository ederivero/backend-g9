# el try va de la mano con el except, no pueden ir separados
from typing import final


try:
    # si no se emite ningun error dentro del try JAMAS ingresara al except
    # print(10/0)
    int('a')
except ZeroDivisionError:
    # aca ingresara si el error es de tipo ZeroDivisionError
    print('Hubo un error al dividir entre cero')

except ValueError:
    # aca entrara si hubo un error de conversion a entero
    print('Error al convertir el numero')

except Exception as error:
    # aca entrara si el error es otro generico
    # .args > es el atributo de toda instancia de Exception que me devolvera el porque se dio ese error(argumentos)
    print(error.args)
    print('Hubo un error al dividir entre cero')

print('Yo no soy un error')

try:
    # args son los argumentos que nosotros indicaremos o que recibiremos cuando se de un error, en este atributo se podran obtener todos los argumentos del porque se dio ese error
    raise Exception('error desconocido') # throw new Error() > JS
except Exception as error:
    print(error.args)




try:
    resultado = 5/1
    raise Exception('Error desconocido')

except Exception as error:
    print(error.args)

else:
    # en el caso que el codigo se ejecutase sin ningun error (sin ingresar al except)
    print('La operacion se realizo exitosamente')

finally: 
    # ingresa si la ejecucion estuvo bien o si ingreso al except
    print('Si la operacion estuvo bien o mal igual se ejecuta')


# EJERCICIO: 
# Recibir por el teclado un numero 
numero = input('Ingresa un numero: ')

# luego tratar de convertir ese numero a un entero (si no se puede indicar que el valor es incorrecto). Sumar 10 mas ese numero ingresado e imprimir el resultado

try:
    numeroEntero = int(numero)
except ValueError:
    print('El valor ingresado es incorrecto')
else:
    print(numeroEntero + 10)