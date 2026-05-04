# Tokens: IF, ELIF, ELSE
# Implementacion: AUTOMATA

# Estados del automata
ESTADO_INICIAL    = "q0"
ESTADO_VISTO_I    = "q1"    # Leer 'i'
ESTADO_VISTO_IF   = "q2"    # Leer 'if' es una posible keyword IF
ESTADO_VISTO_E    = "q3"    # Leer 'e'
ESTADO_VISTO_EL   = "q4"    # Leer 'el'
ESTADO_VISTO_ELI  = "q5"    # Leer 'eli'
ESTADO_VISTO_ELIF = "q6"    # Leer 'elif' es una posible keyword ELIF
ESTADO_VISTO_ELS  = "q7"    # Leer 'els'
ESTADO_VISTO_ELSE = "q8"    # Leer 'else'
ESTADO_NOMBRE     = "qn"    # Identificador (NAME)

# Funciones auxiliares para caracteres

def es_letra(caracter):
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_guion_bajo(caracter):
    return caracter == '_'

def puede_continuar_identificador(caracter):
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)
# Transicion desde keyword

def transicion_desde_posible_keyword(caracter_actual, lexema_reconocido):
    if puede_continuar_identificador(caracter_actual):
        return (ESTADO_NOMBRE, lexema_reconocido + caracter_actual)
    else:
        return (None, lexema_reconocido)

# Funcion principal del automata

def reconocer_condicional(cadena_de_entrada):

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

            if caracter_actual == 'i':
                estado_actual     = ESTADO_VISTO_I
                lexema_reconocido += caracter_actual

            elif caracter_actual == 'e':
                estado_actual     = ESTADO_VISTO_E
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                return (False, "ERROR", caracter_actual,
                        f"Error: '{caracter_actual}' no es un carácter de inicio válido.")

        # Estado q1
        elif estado_actual == ESTADO_VISTO_I:

            if caracter_actual == 'f':
                estado_actual     = ESTADO_VISTO_IF
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break

        # Estado q2
        elif estado_actual == ESTADO_VISTO_IF:

            nuevo_estado, lexema_reconocido = transicion_desde_posible_keyword(caracter_actual, lexema_reconocido)

            if nuevo_estado is None:
                break
            else:
                estado_actual = nuevo_estado

        # Estado q3
        elif estado_actual == ESTADO_VISTO_E:

            if caracter_actual == 'l':
                estado_actual     = ESTADO_VISTO_EL
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break

        # Estado q4
        elif estado_actual == ESTADO_VISTO_EL:

            if caracter_actual == 'i':
                estado_actual     = ESTADO_VISTO_ELI
                lexema_reconocido += caracter_actual

            elif caracter_actual == 's':
                estado_actual     = ESTADO_VISTO_ELS
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break

        # Estado q5
        elif estado_actual == ESTADO_VISTO_ELI:

            if caracter_actual == 'f':
                estado_actual     = ESTADO_VISTO_ELIF
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break

        # Estado q6
        elif estado_actual == ESTADO_VISTO_ELIF:

            nuevo_estado, lexema_reconocido = transicion_desde_posible_keyword(caracter_actual, lexema_reconocido)

            if nuevo_estado is None:
                break
            else:
                estado_actual = nuevo_estado

        # Estado q7
        elif estado_actual == ESTADO_VISTO_ELS:

            if caracter_actual == 'e':
                estado_actual     = ESTADO_VISTO_ELSE
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break

        # Estado q8
        elif estado_actual == ESTADO_VISTO_ELSE:

            nuevo_estado, lexema_reconocido = transicion_desde_posible_keyword(caracter_actual, lexema_reconocido)

            if nuevo_estado is None:
                break
            else:
                estado_actual = nuevo_estado

        # Estado qn (identificador)
        elif estado_actual == ESTADO_NOMBRE:

            if puede_continuar_identificador(caracter_actual):
                lexema_reconocido += caracter_actual
            else:
                break

        indice_caracter += 1

    # Resultados finales

    if estado_actual == ESTADO_VISTO_IF:
        return (True,  "IF",   lexema_reconocido, "Keyword 'if' reconocida.")

    elif estado_actual == ESTADO_VISTO_ELIF:
        return (True,  "ELIF", lexema_reconocido, "Keyword 'elif' reconocida.")

    elif estado_actual == ESTADO_VISTO_ELSE:
        return (True,  "ELSE", lexema_reconocido, "Keyword 'else' reconocida.")

    elif estado_actual in [ESTADO_NOMBRE, ESTADO_VISTO_I, ESTADO_VISTO_E, ESTADO_VISTO_EL, ESTADO_VISTO_ELI, ESTADO_VISTO_ELS]:
        return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")

    else:
        return (False, "ERROR", lexema_reconocido, "Error: token no reconocido.")




# Pruebas del autómata
if __name__ == "__main__":
    print("  Keywords IF  ELIF  ELSE")
    print("  Escribe 'salir' para terminar")

    while True:

        cadena_ingresada = input("\n  Ingresa una cadena: ")  # input de cadena a analizar

        if cadena_ingresada == "salir":  # Condición de salida del programa
            print("  Programa terminado.")
            break

        es_keyword, tipo_token, lexema, mensaje = reconocer_condicional(cadena_ingresada)

        print(f"  Token    : {tipo_token}")
        print(f"  Lexema   : '{lexema}'")
        print(f"  Mensaje  : {mensaje}")
        print("-" * 60)
