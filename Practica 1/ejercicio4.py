# Ejercicio 4: Manipulación de diferentes tipos de datos
# Escribir un programa que tome una lista de números enteros como entrada del usuario.
# Luego, convertir cada número en la lista a string y unir en una sola cadena, separados por guiones ('-').
# Excluir cualquier número que sea múltiplo de 3 de la cadena final.

# Solicitamos los números al usuario separados por espacios
entrada = input("Ingresá números enteros separados por espacios: ")

# Separamos la cadena ingresada en elementos individuales usando split()
valores = entrada.split()

# Convertimos cada elemento a número entero
numeros = []
for valor in valores:
    numeros.append(int(valor))

# Filtramos los números que NO sean múltiplos de 3 y los convertimos a string
numeros_filtrados_str = []
for numero in numeros:
    # Verificamos si no es múltiplo de 3 (el resto de dividir por 3 no es 0)
    if numero % 3 != 0:
        numeros_filtrados_str.append(str(numero))

# Unimos los elementos en una sola cadena separados por guiones '-'
resultado = "-".join(numeros_filtrados_str)

# Mostramos el resultado
print("Cadena resultante:", resultado)
