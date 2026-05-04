# Tokens: PLUS (+), MINUS (-), TIMES (*), POWER (**), DIVIDE (/), FLOORDIV (//), MOD (%)
# Implementacion: AUTOMATA

# Estados del automata
ESTADO_INICIAL      = "q0"
ESTADO_VISTO_STAR   = "q1"
ESTADO_VISTO_SLASH  = "q2"

# Constantes de caracteres

CARACTER_SUMA       = '+'
CARACTER_RESTA      = '-'
CARACTER_ESTRELLA   = '*'
CARACTER_DIAGONAL   = '/'
CARACTER_PORCENTAJE = '%'
# Funcion principal del automata

def reconocer_operador_aritmetico(cadena_de_entrada):

    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    estado_actual = ESTADO_INICIAL
    lexema_reconocido = ""
    indice_caracter = 0

    # Leer la cadena caracter por caracter

    while indice_caracter < len(cadena_de_entrada):

        caracter_actual = cadena_de_entrada[indice_caracter]

        # Estado q0
        if estado_actual == ESTADO_INICIAL:

            if caracter_actual == CARACTER_SUMA:
                lexema_reconocido += caracter_actual
                return (True, "PLUS", lexema_reconocido, "Operador suma reconocido.")

            elif caracter_actual == CARACTER_RESTA:
                lexema_reconocido += caracter_actual
                return (True, "MINUS", lexema_reconocido, "Operador resta reconocido.")

            elif caracter_actual == CARACTER_PORCENTAJE:
                lexema_reconocido += caracter_actual
                return (True, "MOD", lexema_reconocido, "Operador módulo reconocido.")

            elif caracter_actual == CARACTER_ESTRELLA:
                estado_actual     = ESTADO_VISTO_STAR
                lexema_reconocido += caracter_actual

            elif caracter_actual == CARACTER_DIAGONAL:
                estado_actual     = ESTADO_VISTO_SLASH
                lexema_reconocido += caracter_actual

            else:
                return (
                    False,
                    "ERROR",
                    caracter_actual,
                    f"Error léxico: '{caracter_actual}' no es un operador aritmético válido."
                )

        # Estado q1 (*)
        elif estado_actual == ESTADO_VISTO_STAR:

            if caracter_actual == CARACTER_ESTRELLA:
                lexema_reconocido += caracter_actual
                return (True, "POWER", lexema_reconocido, "Operador potencia reconocido.")
            else:
                # Es TIMES, no consumir el caracter actual
                return (True, "TIMES", lexema_reconocido, "Operador multiplicación reconocido.")

        # Estado q2 (/)
        elif estado_actual == ESTADO_VISTO_SLASH:

            if caracter_actual == CARACTER_DIAGONAL:
                lexema_reconocido += caracter_actual
                return (True, "FLOORDIV", lexema_reconocido, "Operador división entera reconocido.")
            else:
                # Es DIVIDE, no consumir el caracter actual
                return (True, "DIVIDE", lexema_reconocido, "Operador división reconocido.")

        indice_caracter += 1

    # Resultados finales

    if estado_actual == ESTADO_VISTO_STAR:
        return (True, "TIMES", lexema_reconocido, "Operador multiplicación reconocido.")

    elif estado_actual == ESTADO_VISTO_SLASH:
        return (True, "DIVIDE", lexema_reconocido, "Operador división reconocido.")

    else:
        return (False, "ERROR", lexema_reconocido, "Error: no se pudo reconocer el operador.")




# Pruebas del autómata
if __name__ == "__main__":
    print("  Operadores Aritméticos")
    print("  Tokens: PLUS  MINUS  TIMES  POWER  DIVIDE  FLOORDIV  MOD")
    print("  Escribe 'salir' para terminar.")

    while True:

        cadena_ingresada = input("\n  Ingresa una cadena: ")  # input de cadena a analizar

        if cadena_ingresada == "salir":  # Condición de salida del programa
            print("  Programa terminado.")
            break

        es_valido, tipo_token, lexema, mensaje = reconocer_operador_aritmetico(cadena_ingresada)

        print(f"  Token    : {tipo_token}")
        print(f"  Lexema   : '{lexema}'")
        print(f"  Mensaje  : {mensaje}")
        print("-" * 60)
