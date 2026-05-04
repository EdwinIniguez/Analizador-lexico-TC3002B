# Token: NAME
# Implementacion: AUTOMATA

# Estados del automata
ESTADO_INICIAL = "q0"
ESTADO_VALIDO  = "q1"
ESTADO_ERROR   = "qe"

# Funciones auxiliares para caracteres

def es_letra(caracter):
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_guion_bajo(caracter):
    return caracter == '_'

def puede_iniciar_identificador(caracter):
    return es_letra(caracter) or es_guion_bajo(caracter)

def puede_continuar_identificador(caracter):
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)
# Funcion principal del automata

def reconocer_identificador(cadena_de_entrada):

    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    estado_actual = ESTADO_INICIAL
    lexema_reconocido = ""
    indice_caracter = 0

    # Leer la cadena caracter por caracter

    while indice_caracter < len(cadena_de_entrada):

        caracter_actual = cadena_de_entrada[indice_caracter]

        # Estado inicial q0
        if estado_actual == ESTADO_INICIAL:

            if puede_iniciar_identificador(caracter_actual):
                estado_actual     = ESTADO_VALIDO  # q1
                lexema_reconocido += caracter_actual
            else:
                estado_actual     = ESTADO_ERROR
                lexema_reconocido += caracter_actual

        # Estado valido q1
        elif estado_actual == ESTADO_VALIDO:

            if puede_continuar_identificador(caracter_actual):
                lexema_reconocido += caracter_actual
            else:
                break

        # Estado error qe
        elif estado_actual == ESTADO_ERROR:
            break

        indice_caracter += 1

    # Resultados finales

    if estado_actual == ESTADO_VALIDO:
        return (
            True,
            "NAME",
            lexema_reconocido,
            "Token válido"
        )

    elif estado_actual == ESTADO_ERROR:
        return (
            False,
            "ERROR",
            lexema_reconocido,
            "Error: identificador no válido."
        )

    else:
        return (
            False,
            "ERROR",
            "",
            "Error: no se pudo reconocer ningún caracter."
        )




# Pruebas del autómata
if __name__ == "__main__":
    print("  Identificadores -> NAME")
    print("  Escribe salir para terminar.")


    while True:

        cadena_ingresada = input("\n  Ingresa una cadena: ")  # input de cadena a analizar

        if cadena_ingresada == "salir":  # Condición de salida del programa
            break

        es_valido, tipo_token, lexema, mensaje = reconocer_identificador(cadena_ingresada)

        print(f"  Token    : {tipo_token}")
        print(f"  Lexema   : '{lexema}'")
        print(f"  Mensaje  : {mensaje}")
        print("-" * 60)
