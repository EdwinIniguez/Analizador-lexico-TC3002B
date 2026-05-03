# Tokens reconocidos: PLUSEQ (+=), MINUSEQ (-=), TIMESEQ (*=), DIVEQ (/=)
# Tipo de implementación: REGEX
#
# Las expresiones regulares para estos operadores se programan comparando la cadena de entrada caracter por caracter.
#
#   RE para PLUSEQ  →  +=
#   RE para MINUSEQ →  -=
#   RE para TIMESEQ →  *=
#   RE para DIVEQ   →  /=


# Función auxiliar compartida que es común para todos los operadores de asignación

def comparar_operador(cadena_de_entrada, operador_esperado, nombre_token):

    # Parámetros: cadena_de_entrada (str): La cadena que se desea analizar. operador_esperado (str): El operador a comparar.
    # nombre_token (str): El nombre del token (ej. "PLUSEQ", "MINUSEQ").

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
            # Si hay más caracteres después del operador (ej: "+=5"), el lexema solo abarca el operador.
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
def reconocer_pluseq(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "+=", "PLUSEQ")

def reconocer_minuseq(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "-=", "MINUSEQ")

def reconocer_timeseq(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "*=", "TIMESEQ")

def reconocer_diveq(cadena_de_entrada):
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_operador(cadena_de_entrada, "/=", "DIVEQ")




# Función para detectar automáticamente cuál operador de asignación compuesto intentar

def reconocer_operadores_asignacion_compuesta(cadena_de_entrada):

    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    primera_letra = cadena_de_entrada[0]

    if primera_letra == '+':
        return reconocer_pluseq(cadena_de_entrada)

    elif primera_letra == '-':
        return reconocer_minuseq(cadena_de_entrada)

    elif primera_letra == '*':
        return reconocer_timeseq(cadena_de_entrada)

    elif primera_letra == '/':
        return reconocer_diveq(cadena_de_entrada)

    return (False, "ERROR", cadena_de_entrada, f"Error: '{cadena_de_entrada}' no es un operador de asignación compuesta válido.")




# Pruebas de las regex
print("  Tokens de asignación compuesta: PLUSEQ (+=)  MINUSEQ (-=)  TIMESEQ (*=)  DIVEQ (/=)")
print("  Escribe 'salir' para terminar.")

while True:

    cadena_ingresada = input("\n  Ingresa una cadena: ")

    if cadena_ingresada == "salir":
        print("  Programa terminado.")
        break

    es_operador, tipo_token, lexema, mensaje = reconocer_operadores_asignacion_compuesta(cadena_ingresada)

    print(f"  Token    : {tipo_token}")
    print(f"  Lexema   : '{lexema}'")
    print(f"  Mensaje  : {mensaje}")
    print("-" * 60)