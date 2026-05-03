# Tokens reconocidos: COMMA (,), COLON (:), DOT (.), AT (@), ARROW (->), TILDE (~), AMPERSAND (&), PIPE (`), CARET (^), LSHIFT (<<), RSHIFT (>>)
# Tipo de implementación: REGEX
#
# Las expresiones regulares para estos símbolos se programan comparando la cadena de entrada caracter por caracter.
#
#   RE para COMMA     →  ,
#   RE para COLON     →  :
#   RE para DOT       →  .
#   RE para AT        →  @
#   RE para ARROW     →  ->
#   RE para TILDE     →  ~
#   RE para AMPERSAND →  &
#   RE para PIPE      →  `  (Acento grave según especificación)
#   RE para CARET     →  ^
#   RE para LSHIFT    →  <<
#   RE para RSHIFT    →  >>


# Función auxiliar compartida que es común para todos los símbolos especiales

def comparar_simbolo(cadena_de_entrada, simbolo_esperado, nombre_token):

    # Parámetros: cadena_de_entrada (str): La cadena que se desea analizar. simbolo_esperado (str): El símbolo a comparar.
    # nombre_token (str): El nombre del token (ej. "COMMA", "ARROW").

    # Retorna tuple: (es_simbolo, tipo_token, lexema_reconocido, mensaje_resultado)

    longitud_simbolo = len(simbolo_esperado)
    longitud_entrada = len(cadena_de_entrada)

    lexema_reconocido = ""  # String para ir guardando el texto introducido

    indice_caracter = 0  # Índice para ver en qué caracter estamos



    # ------------------------------------------------------->  LEER LA CADENA CARACTER POR CARACTER <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    while indice_caracter < longitud_entrada:

        caracter_actual   = cadena_de_entrada[indice_caracter]
        lexema_reconocido += caracter_actual


        # Verificar si aún estamos comparando contra el símbolo <--------------------------------------------------------
        if indice_caracter < longitud_simbolo:

            caracter_simbolo = simbolo_esperado[indice_caracter]  # Caracter esperado en esta posición

            if caracter_actual != caracter_simbolo:
                return (False, "ERROR", lexema_reconocido, f"Error: '{lexema_reconocido}' no coincide con el símbolo esperado.")
                

        # Ya terminamos de comparar los caracteres del símbolo <--------------------------------------------------------
        elif indice_caracter == longitud_simbolo:
            # Si hay más caracteres después del símbolo (ej: "->x"), el lexema solo abarca el símbolo.
            # Removemos el caracter extra que se concatenó en este ciclo.
            lexema_reconocido = lexema_reconocido[:-1]
            break


        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    if lexema_reconocido == simbolo_esperado:
        return (True, nombre_token, lexema_reconocido, f"Símbolo '{simbolo_esperado}' reconocido.")
    else:
        return (False, "ERROR", lexema_reconocido, "Error: no se pudo reconocer el símbolo completamente.")




# Funciones individuales por símbolo, cada una llama a comparar_simbolo
def reconocer_comma(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, ",", "COMMA")

def reconocer_colon(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, ":", "COLON")

def reconocer_dot(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, ".", "DOT")

def reconocer_at(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, "@", "AT")

def reconocer_arrow(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, "->", "ARROW")

def reconocer_tilde(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, "~", "TILDE")

def reconocer_ampersand(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, "&", "AMPERSAND")

def reconocer_pipe(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, "`", "PIPE")

def reconocer_caret(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, "^", "CARET")

def reconocer_lshift(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, "<<", "LSHIFT")

def reconocer_rshift(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_simbolo(cadena_de_entrada, ">>", "RSHIFT")




# Función para detectar automáticamente cuál símbolo intentar

def reconocer_simbolo_especial(cadena_de_entrada):

    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    primera_letra = cadena_de_entrada[0]

    if primera_letra == ',':
        return reconocer_comma(cadena_de_entrada)

    elif primera_letra == ':':
        return reconocer_colon(cadena_de_entrada)

    elif primera_letra == '.':
        return reconocer_dot(cadena_de_entrada)

    elif primera_letra == '@':
        return reconocer_at(cadena_de_entrada)

    elif primera_letra == '-':
        if len(cadena_de_entrada) >= 2 and cadena_de_entrada[1] == '>':
            return reconocer_arrow(cadena_de_entrada)
        return (False, "ERROR", primera_letra, "Error: el caracter '-' por sí solo no es válido en este contexto (se espera '->').")

    elif primera_letra == '~':
        return reconocer_tilde(cadena_de_entrada)

    elif primera_letra == '&':
        return reconocer_ampersand(cadena_de_entrada)

    elif primera_letra == '`':
        return reconocer_pipe(cadena_de_entrada)

    elif primera_letra == '^':
        return reconocer_caret(cadena_de_entrada)

    elif primera_letra == '<':
        if len(cadena_de_entrada) >= 2 and cadena_de_entrada[1] == '<':
            return reconocer_lshift(cadena_de_entrada)
        return (False, "ERROR", primera_letra, "Error: el caracter '<' por sí solo no es válido en este contexto (se espera '<<').")

    elif primera_letra == '>':
        if len(cadena_de_entrada) >= 2 and cadena_de_entrada[1] == '>':
            return reconocer_rshift(cadena_de_entrada)
        return (False, "ERROR", primera_letra, "Error: el caracter '>' por sí solo no es válido en este contexto (se espera '>>').")

    return (False, "ERROR", cadena_de_entrada, f"Error: '{cadena_de_entrada}' no es un símbolo válido.")




# Pruebas de las regex
print("  Tokens de símbolos especiales:")
print("  COMMA (,)  COLON (:)  DOT (.)  AT (@)  ARROW (->)  TILDE (~)")
print("  AMPERSAND (&)  PIPE (`)  CARET (^)  LSHIFT (<<)  RSHIFT (>>)")
print("  Escribe 'salir' para terminar.")

while True:

    cadena_ingresada = input("\n  Ingresa una cadena: ")

    if cadena_ingresada == "salir":
        print("  Programa terminado.")
        break

    es_simbolo, tipo_token, lexema, mensaje = reconocer_simbolo_especial(cadena_ingresada)

    print(f"  Token    : {tipo_token}")
    print(f"  Lexema   : '{lexema}'")
    print(f"  Mensaje  : {mensaje}")
    print("-" * 60)