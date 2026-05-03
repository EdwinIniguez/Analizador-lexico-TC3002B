# Tokens reconocidos: LPAREN ((), RPAREN ()), LBRACKET ([), RBRACKET (]), LBRACE ({), RBRACE (})
# Tipo de implementación: REGEX
#
# Las expresiones regulares para estos delimitadores se programan comparando la cadena de entrada caracter por caracter.
#
#   RE para LPAREN   →  (
#   RE para RPAREN   →  )
#   RE para LBRACKET →  [
#   RE para RBRACKET →  ]
#   RE para LBRACE   →  {
#   RE para RBRACE   →  }


# Función auxiliar compartida que es común para todos los delimitadores

def comparar_delimitador(cadena_de_entrada, delimitador_esperado, nombre_token):

    # Parámetros: cadena_de_entrada (str): La cadena que se desea analizar. delimitador_esperado (str): El delimitador a comparar.
    # nombre_token (str): El nombre del token (ej. "LPAREN", "RBRACKET").

    # Retorna tuple: (es_delimitador, tipo_token, lexema_reconocido, mensaje_resultado)

    longitud_delimitador = len(delimitador_esperado)
    longitud_entrada     = len(cadena_de_entrada)

    lexema_reconocido = ""  # String para ir guardando el texto introducido

    indice_caracter = 0  # Índice para ver en qué caracter estamos



    # ------------------------------------------------------->  LEER LA CADENA CARACTER POR CARACTER <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    while indice_caracter < longitud_entrada:

        caracter_actual   = cadena_de_entrada[indice_caracter]
        lexema_reconocido += caracter_actual


        # Verificar si aún estamos comparando contra el delimitador <--------------------------------------------------------
        if indice_caracter < longitud_delimitador:

            caracter_delimitador = delimitador_esperado[indice_caracter]  # Caracter esperado en esta posición

            if caracter_actual != caracter_delimitador:
                return (False, "ERROR", lexema_reconocido, f"Error: '{lexema_reconocido}' no coincide con el delimitador esperado.")
                

        # Ya terminamos de comparar los caracteres del delimitador <--------------------------------------------------------
        elif indice_caracter == longitud_delimitador:
            # Si hay más caracteres después del delimitador (ej: "(x"), el lexema solo abarca el delimitador.
            # Removemos el caracter extra que se concatenó en este ciclo.
            lexema_reconocido = lexema_reconocido[:-1]
            break


        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    if lexema_reconocido == delimitador_esperado:
        return (True, nombre_token, lexema_reconocido, f"Delimitador '{delimitador_esperado}' reconocido.")
    else:
        return (False, "ERROR", lexema_reconocido, "Error: no se pudo reconocer el delimitador completamente.")




# Funciones individuales por delimitador, cada una llama a comparar_delimitador
def reconocer_lparen(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_delimitador(cadena_de_entrada, "(", "LPAREN")

def reconocer_rparen(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_delimitador(cadena_de_entrada, ")", "RPAREN")

def reconocer_lbracket(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_delimitador(cadena_de_entrada, "[", "LBRACKET")

def reconocer_rbracket(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_delimitador(cadena_de_entrada, "]", "RBRACKET")

def reconocer_lbrace(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_delimitador(cadena_de_entrada, "{", "LBRACE")

def reconocer_rbrace(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_delimitador(cadena_de_entrada, "}", "RBRACE")




# Función para detectar automáticamente cuál delimitador intentar

def reconocer_delimitador(cadena_de_entrada):

    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    primera_letra = cadena_de_entrada[0]

    if primera_letra == '(':
        return reconocer_lparen(cadena_de_entrada)

    elif primera_letra == ')':
        return reconocer_rparen(cadena_de_entrada)

    elif primera_letra == '[':
        return reconocer_lbracket(cadena_de_entrada)

    elif primera_letra == ']':
        return reconocer_rbracket(cadena_de_entrada)

    elif primera_letra == '{':
        return reconocer_lbrace(cadena_de_entrada)

    elif primera_letra == '}':
        return reconocer_rbrace(cadena_de_entrada)

    return (False, "ERROR", cadena_de_entrada, f"Error: '{cadena_de_entrada}' no es un delimitador válido.")




# Pruebas de las regex
print("  Tokens de delimitadores: LPAREN (()  RPAREN ())  LBRACKET ([)  RBRACKET (])  LBRACE ({)  RBRACE (})")
print("  Escribe 'salir' para terminar.")

while True:

    cadena_ingresada = input("\n  Ingresa una cadena: ")

    if cadena_ingresada == "salir":
        print("  Programa terminado.")
        break

    es_delimitador, tipo_token, lexema, mensaje = reconocer_delimitador(cadena_ingresada)

    print(f"  Token    : {tipo_token}")
    print(f"  Lexema   : '{lexema}'")
    print(f"  Mensaje  : {mensaje}")
    print("-" * 60)