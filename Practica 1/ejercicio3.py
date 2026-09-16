# lista generada en el ejercicio 1
lista_numeros = [10, 15, 23, 30, 42, 50, 61, 100]
# Le pedimos el múltiplo al usuario (convertido a entero con int)
multiplo = int(input("Ingresá un número para buscar sus múltiplos: "))
lista_NOmultiplos =[]
lista_multiplos = []

print(f" Analizando Los múltiplos de {multiplo} en la lista..")

    # Recorremos la lista elemento por elemento
for numero in lista_numeros:
    # Verificamos si no es múltiplo (el resto de la división no es 0)
    if numero % multiplo != 0:
        lista_NOmultiplos.append(numero)
    else:
        lista_multiplos.append(numero)

print("la lista de multiplos es: ", lista_multiplos)
print("la lista de NO multiplos es: ", lista_NOmultiplos)




