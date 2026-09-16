# lista con números cualquiera
lista_numeros = [10, 15, 23, 30, 42, 50, 61, 100]

# Le pedimos el múltiplo al usuario (convertido a entero con int)
multiplo = int(input("Ingresá un número para buscar sus múltiplos: "))

print(f"Los múltiplos de {multiplo} en la lista son:")

# Recorremos la lista elemento por elemento
for numero in lista_numeros:
    # Verificamos si no es múltiplo (el resto de la división no es 0)
    if numero % multiplo != 0:
        continue  # Aborta esta iteración y salta al siguiente número de la lista
    
    # Si la condición de arriba se cumplió y se ejecutó el 'continue', 
    # Python ignora todo lo que haya abajo.
    # Por lo tanto, si el código llega a este print, sabemos seguro que SÍ es múltiplo.
    print(numero)