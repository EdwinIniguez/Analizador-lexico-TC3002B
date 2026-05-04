# Token: STRING
# Implementacion: AUTOMATA

# Estados del automata
ESTADO_INICIAL       = "q0"
ESTADO_LEYENDO       = "q1"
ESTADO_CADENA_CIERRA = "q2"
ESTADO_ERROR         = "qe"

# Constantes de caracteres

COMILLA_DOBLE  = '"'
SALTO_DE_LINEA = '\n'
# Funcion principal del automata

def reconocer_cadena(cadena_de_entrada):

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

            if caracter_actual == COMILLA_DOBLE:
                estado_actual     = ESTADO_LEYENDO
                lexema_reconocido += caracter_actual
            else:
                estado_actual     = ESTADO_ERROR
                lexema_reconocido += caracter_actual

        # Estado q1
        elif estado_actual == ESTADO_LEYENDO:

            if caracter_actual == COMILLA_DOBLE:
                estado_actual     = ESTADO_CADENA_CIERRA
                lexema_reconocido += caracter_actual
                indice_caracter   += 1
                break
            elif caracter_actual == SALTO_DE_LINEA:
                estado_actual = ESTADO_ERROR
                break
            else:
                lexema_reconocido += caracter_actual

        # Estado error qe
        elif estado_actual == ESTADO_ERROR:
            break

        indice_caracter += 1

    if estado_actual == ESTADO_LEYENDO:
        estado_actual = ESTADO_ERROR

    # Resultados finales

    if estado_actual == ESTADO_CADENA_CIERRA:
        return (
            True,
            "STRING",
            lexema_reconocido,
            "Cadena de texto válida reconocida."
        )

    elif estado_actual == ESTADO_ERROR and lexema_reconocido.startswith(COMILLA_DOBLE):
        return (
            False,
            "ERROR",
            lexema_reconocido,
            'Error: cadena no terminada. Falta la comilla de cierre (").'
        )

    else:
        return (
            False,
            "ERROR",
            lexema_reconocido,
            'Error: una cadena debe iniciar con comilla doble (").'
        )




# Pruebas del autómata
if __name__ == "__main__":
    print("  Cadenas de texto (STRING)")
    print("  Escribe 'salir' para terminar")

    while True:

        cadena_ingresada = input("\n  Ingresa una cadena: ")  # input de cadena a analizar

        if cadena_ingresada == "salir":  # Condición de salida del programa
            print("  Programa terminado.")
            break

        es_valido, tipo_token, lexema, mensaje = reconocer_cadena(cadena_ingresada)

        print(f"  Token    : {tipo_token}")
        print(f"  Lexema   : {lexema}")
        print(f"  Mensaje  : {mensaje}")
        print("-" * 60)
