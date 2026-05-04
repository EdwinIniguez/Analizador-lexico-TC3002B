# Tokens: PLUSEQ (+=), MINUSEQ (-=), TIMESEQ (*=), DIVEQ (/=)
# Implementacion: REGEX

# Funcion auxiliar para operadores de asignacion

def comparar_operador(cadena_de_entrada, operador_esperado, nombre_token):

    # Parametros: cadena, operador esperado y nombre del token
    # Retorna: (es_valido, tipo_token, lexema, mensaje)

    longitud_operador = len(operador_esperado)
    longitud_entrada  = len(cadena_de_entrada)

    lexema_reconocido = ""
    indice_caracter = 0

    # Leer la cadena caracter por caracter

    while indice_caracter < longitud_entrada:

        caracter_actual   = cadena_de_entrada[indice_caracter]
        lexema_reconocido += caracter_actual

        # Verificar coincidencia con el operador
        if indice_caracter < longitud_operador:

            caracter_operador = operador_esperado[indice_caracter]

            if caracter_actual != caracter_operador:
                return (False, "ERROR", lexema_reconocido, f"Error: '{lexema_reconocido}' no coincide con el operador esperado.")
                
        # Operador terminado
        elif indice_caracter == longitud_operador:
            # Evitar consumir caracteres extra
            lexema_reconocido = lexema_reconocido[:-1]
            break

        indice_caracter += 1

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
if __name__ == "__main__":
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