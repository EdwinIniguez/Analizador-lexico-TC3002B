# Tokens reconocidos: LT (<), GT (>), LE (<=), GE (>=), EQ (==), NE (!=), ASSIGN (=)
# Tipo de implementación: REGEX
#
# Las expresiones regulares para estos operadores se programan comparando la cadena de entrada caracter por caracter.
#
#   RE para LT     →  <
#   RE para GT     →  >
#   RE para LE     →  <=
#   RE para GE     →  >=
#   RE para EQ     →  ==
#   RE para NE     →  !=
#   RE para ASSIGN →  =


# Función auxiliar compartida que es común para todos los operadores relacionales

def comparar_operador(cadena_de_entrada, operador_esperado, nombre_token):

    # Parámetros: cadena_de_entrada (str): La cadena que se desea analizar. operador_esperado (str): El operador a comparar.
    # nombre_token (str): El nombre del token (ej. "LE", "EQ").

    # Retorna tuple: (es_operador, tipo_token, lexema_reconocido, mensaje_resultado)

    longitud_operador = len(operador_esperado)
    longitud_entrada  = len(cadena_de_entrada)

    lexema_reconocido = ""  # String para ir guardando el texto introducido

    indice_caracter = 0  # Índice para ver en qué caracter estamos



    # ------------------------------------------------------->  LEER LA CADENA CARACTER POR CARACTER <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    while indice_caracter < longitud_entrada:

        caracter_actual   = cadena_de_entrada[indice_caracter]
        lexema_reconocido += caracter_actual


        # Verificar si aún estamos comparando contra el operador <--------------------------------------------------------
        if indice_caracter < longitud_operador:

            caracter_operador = operador_esperado[indice_caracter]  # Caracter esperado en esta posición

            if caracter_actual != caracter_operador:
                return (False, "ERROR", lexema_reconocido, f"Error: '{lexema_reconocido}' no coincide con el operador esperado.")
                

        # Ya terminamos de comparar los caracteres del operador <--------------------------------------------------------
        elif indice_caracter == longitud_operador:
            # Si hay más caracteres después del operador (ej: "<=5"), el lexema solo abarca el operador.
            # Removemos el caracter extra que se concatenó en este ciclo.
            lexema_reconocido = lexema_reconocido[:-1]
            break


        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    if lexema_reconocido == operador_esperado:
        return (True, nombre_token, lexema_reconocido, f"Operador '{operador_esperado}' reconocido.")
    else:
        return (False, "ERROR", lexema_reconocido, "Error: no se pudo reconocer el operador completamente.")




# Funciones individuales por operador, cada una llama a comparar_operador
def reconocer_lt(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "<", "LT")

def reconocer_gt(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, ">", "GT")

def reconocer_le(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "<=", "LE")

def reconocer_ge(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, ">=", "GE")

def reconocer_eq(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "==", "EQ")

def reconocer_ne(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "!=", "NE")

def reconocer_assign(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "=", "ASSIGN")




# Diccionarios para los operadores compuestos dependiendo de su caracter secundario
OPERADORES_CON_MENOR_QUE = {
    '=': reconocer_le,
}

OPERADORES_CON_MAYOR_QUE = {
    '=': reconocer_ge,
}

OPERADORES_CON_IGUAL = {
    '=': reconocer_eq,
}




# Función para detectar automáticamente cuál operador relacional intentar

def reconocer_operadores_relacionales_regex(cadena_de_entrada):

    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    primera_letra = cadena_de_entrada[0]

    if primera_letra == '<':
        if len(cadena_de_entrada) >= 2 and cadena_de_entrada[1] in OPERADORES_CON_MENOR_QUE:
            return OPERADORES_CON_MENOR_QUE[cadena_de_entrada[1]](cadena_de_entrada)
        return reconocer_lt(cadena_de_entrada)

    elif primera_letra == '>':
        if len(cadena_de_entrada) >= 2 and cadena_de_entrada[1] in OPERADORES_CON_MAYOR_QUE:
            return OPERADORES_CON_MAYOR_QUE[cadena_de_entrada[1]](cadena_de_entrada)
        return reconocer_gt(cadena_de_entrada)

    elif primera_letra == '=':
        if len(cadena_de_entrada) >= 2 and cadena_de_entrada[1] in OPERADORES_CON_IGUAL:
            return OPERADORES_CON_IGUAL[cadena_de_entrada[1]](cadena_de_entrada)
        return reconocer_assign(cadena_de_entrada)

    elif primera_letra == '!':
        if len(cadena_de_entrada) >= 2 and cadena_de_entrada[1] == '=':
            return reconocer_ne(cadena_de_entrada)
        return (False, "ERROR", "!", "Error: el caracter '!' por sí solo no es válido en este contexto.")

    return (False, "ERROR", cadena_de_entrada, f"Error: '{cadena_de_entrada}' no es un operador relacional válido.")




# Pruebas de las regex
print("  Tokens relacionales: LT (<)  GT (>)  LE (<=)  GE (>=)  EQ (==)  NE (!=)  ASSIGN (=)")
print("  Escribe 'salir' para terminar.")

while True:

    cadena_ingresada = input("\n  Ingresa una cadena: ")

    if cadena_ingresada == "salir":
        print("  Programa terminado.")
        break

    es_operador, tipo_token, lexema, mensaje = reconocer_operadores_relacionales_regex(cadena_ingresada)

    print(f"  Token    : {tipo_token}")
    print(f"  Lexema   : '{lexema}'")
    print(f"  Mensaje  : {mensaje}")
    print("-" * 60)