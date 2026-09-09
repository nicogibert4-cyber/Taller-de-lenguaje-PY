# 1. Creamos una lista con números cualquiera
numeros = [10, 15, 23, 30, 42, 50, 61, 100]

# 2. Le pedimos el múltiplo al usuario (convertido a entero con int)
multiplo = int(input("Ingresá un número para buscar sus múltiplos: "))

print(f"Los múltiplos de {multiplo} en la lista son:")

# 3. Recorremos la lista elemento por elemento
for numero in numeros:
    # Verificamos si NO es múltiplo (el resto de la división no es 0)
    if numero % multiplo != 0:
        continue  # Aborta esta iteración y salta al siguiente número de la lista
    
    # Si la condición de arriba se cumplió y se ejecutó el 'continue', 
    # Python ignora todo lo que haya abajo.
    # Por lo tanto, si el código llega a este print, sabemos seguro que SÍ es múltiplo.
    print(numero)