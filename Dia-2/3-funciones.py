def sumar(num1, num2, num3):
    return num1 + num2 + num3


def sumar_n_numeros(*args):
    # args > arguments sera recibir N (ilimitado) numero de parametros
    print(args)
    # sumar todos los valores de la tupla args utilizando un for
    total = 0
    # Utilizando el contenido de la tupla directamente
    for numero in args:
        total = total + numero
    
    # Usando los numeros de las posiciones
    total2= 0    
    for posicion in range(len(args)):
        total2 = total2 + args[posicion]
    
    print(total2)
    return total

print(sumar(5,10, 7))

resultado = sumar_n_numeros(10,5,18,7,22,56,89)
print(resultado)

resultado = sumar_n_numeros(10,5,18,7,22,56,89,15,14,13,15,18,19,14,17,20)
print(resultado)

def inscribir_personas(persona):
    print(persona)