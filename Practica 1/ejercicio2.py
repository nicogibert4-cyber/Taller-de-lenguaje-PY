# numeros en una sola linea
entrada = input("Ingresa varios numeros separados por espacios: ")

# .split() corta el texto donde hay espacios y nos devuelve una lista
lista_textos = entrada.split()

# Creamos una lista vacia para guardar los numeros reales (enteros)
numeros = []

# Convertimos cada texto a numero y lo agregamos a nuestra nueva lista
for texto in lista_textos:
    numeros.append(int(texto))

print("Iniciando impresion:")

#  Recorremos la lista ya convertida a enteros
for numero in numeros:
    # Verificamos si el numero es negativo
    if numero < 0:
        print("Encontre un numero negativo. Se cancela la impresion.")
        break  # Rompe el ciclo for por completo
    
    # Si no es negativo, simplemente lo imprimimos
    print(numero)
# 1. Repetir una accion 3 veces exactas
print("Ejemplo 1:")
for i in range(3):
    print("Esta frase se imprime tres veces")

# 2. Contar del 1 al 5
print("Ejemplo 2:")
for numero in range(1, 6):
    print(numero)

# 3. Cuenta regresiva del 10 al 1 (usando salto negativo)
print("Ejemplo 3:")
for numero in range(10, 0, -1):
    print(numero)