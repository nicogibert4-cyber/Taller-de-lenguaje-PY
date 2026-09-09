email = input("Ingrese un email: ")

# Asumimos que es valido hasta que se demuestre lo contrario
es_valido = True
mensaje_error = ""

# 1. Contiene exactamente un @
if email.count("@") != 1:
    es_valido = False
    mensaje_error = "debe contener exactamente un @"
else:
    # Cortamos el texto en el @
    partes = email.split("@")
    usuario = partes[0]
    servidor = partes[1]

    # 4. No empieza ni termina con @ ni con .
    if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
        es_valido = False
        mensaje_error = "no puede empezar ni terminar con @ o punto"
        
    # 2. Tiene al menos un caracter antes del @
    elif len(usuario) < 1:
        es_valido = False
        mensaje_error = "debe contener nombre del usuario antes del @"
        
    # 3. Tiene al menos un punto (.) despues del @
    elif "." not in servidor:
        es_valido = False
        mensaje_error = "debe tener un dominio"
        
    # 5. La parte despues del ultimo punto tiene al menos 2 caracteres
    else:
        partes_punto = servidor.split(".")
        extension = partes_punto[-1] # El indice -1 trae el ultimo elemento de la lista
        if len(extension) < 2:
            es_valido = False
            mensaje_error = "el dominio debe tener al menos 2 caracteres"

# Resultado final
if es_valido:
    print(f"{email} VALIDO (OK)")
else:
    print(f"{email} INVALIDO ({mensaje_error})")