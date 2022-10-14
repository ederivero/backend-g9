# Operadores aritmeticos
numero1, numero2 = 10, 50 

# SUMA
# Nota: solamente sera suma si las dos variables son numericas, si es que son string entonces se hara una concatenacion y ademas no se puede sumar entre string y numeros
print(numero1 + numero2)

# RESTA
# Nota: Solamente para numeros
print(numero1 - numero2)
# print('ab' - 'bc') 

# MULTIPLICACION
# Nota: si se usa la multiplicacion en un string, entonces este repetira el numero de veces entre un string y un numero de veces
print(numero1 * numero2)
print('hola'*5)

# DIVISION
print(numero1 / numero2)

# MODULO
print(numero1 % numero2)

# COCIENTE
print(numero1 // numero2)

# EXPONENTE
# 10^50
print(numero1 ** numero2)

# RAIZ CUADRADA usando exponente
print(numero1 ** 0.5)


# -----------------------------------
# OPERADORES ASIGNACION
# IGUAL asignar un nuevo valor a una variable
numero1 = 100

# INCREMENTO
numero1 += 1 # incrementando el valor del numero1 en una unidad
print(numero1)

# DECREMENTO
numero1 -= 1 # numero1 = numero1 - 1
print(numero1)

# MULTIPLICADOR
numero1 *= 2
print(numero1)

# DIVIDENDO
numero1 /= 5 # numero1 = numero1 / 5


# -------------------------------------
# OPERADORES DE COMPARACION Siempre retornaran un booleano (si es verdadero o si es falso)

# IGUAL QUE
# Nota: en python, a diferencia de JS, no existe el triple igual (comparador de tipos de datos)
print(numero1) # Float
print(numero2) # Int
print(numero1 == numero2)
print(int(40.7)) # asi se convierte el tipo de dato
# int('eduardo') # no se puede convertir tipos de datos irreales
print(type(numero1) == type(numero2))

# MAYOR | MAYOR O IGUAL
print(10 > 9.58)
print(10 > int('5'))
print(50 >= 30)

# MENOR | MENOR O IGUAL
print(50 < 80)
print(50 <= 50)
print(50 <= 50)
# Nota: siempre va el simbolo de mayor(>) o menor(<) antes del igual, nunca al revez porque sino python entiende que se esta tratando de una asignacion

print (100>= float("40.24"))