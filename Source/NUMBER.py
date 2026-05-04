# Token: NUMBER (entero o decimal)
# Implementacion: AUTOMATA

# Estados del automata
ESTADO_INICIAL    = "q0"
ESTADO_ENTERO     = "q1"
ESTADO_TRAS_PUNTO = "q2"
ESTADO_DECIMAL    = "q3"
ESTADO_ERROR      = "qe"

# Funciones auxiliares para caracteres

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_punto_decimal(caracter):
    return caracter == '.'
# Funcion principal del automata

def reconocer_numero(cadena_de_entrada):

    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "", "Error: la cadena de entrada está vacía.")

    estado_actual = ESTADO_INICIAL
    lexema_reconocido = ""
    indice_caracter = 0

    # Leer la cadena caracter por caracter

    while indice_caracter < len(cadena_de_entrada):

        caracter_actual = cadena_de_entrada[indice_caracter]

        # Estado q0
        if estado_actual == ESTADO_INICIAL:

            if es_digito(caracter_actual):
                estado_actual     = ESTADO_ENTERO
                lexema_reconocido += caracter_actual
            else:
                estado_actual     = ESTADO_ERROR
                lexema_reconocido += caracter_actual

        # Estado q1
        elif estado_actual == ESTADO_ENTERO:

            if es_digito(caracter_actual):
                lexema_reconocido += caracter_actual
            elif es_punto_decimal(caracter_actual):
                estado_actual     = ESTADO_TRAS_PUNTO
                lexema_reconocido += caracter_actual
            else:
                break

        # Estado q2
        elif estado_actual == ESTADO_TRAS_PUNTO:

            if es_digito(caracter_actual):
                estado_actual     = ESTADO_DECIMAL
                lexema_reconocido += caracter_actual
            else:
                estado_actual = ESTADO_ERROR
                break

        # Estado q3
        elif estado_actual == ESTADO_DECIMAL:

            if es_digito(caracter_actual):
                lexema_reconocido += caracter_actual
            elif es_punto_decimal(caracter_actual):
                estado_actual = ESTADO_ERROR
                break
            else:
                break

        # Estado error qe
        elif estado_actual == ESTADO_ERROR:
            break

        indice_caracter += 1

    # Resultados finales

    if estado_actual == ESTADO_ENTERO:
        return (
            True,
            "NUMBER",
            "ENTERO",
            lexema_reconocido,
            "Número entero reconocido."
        )

    elif estado_actual == ESTADO_DECIMAL:
        return (
            True,
            "NUMBER",
            "DECIMAL",
            lexema_reconocido,
            "Número decimal reconocido."
        )

    elif estado_actual == ESTADO_TRAS_PUNTO:
        return (
            False,
            "ERROR",
            "",
            lexema_reconocido,
            "Error: el punto debe ir seguido de al menos un dígito (ej. 3.14)."
        )

    else:
        return (
            False,
            "ERROR",
            "",
            lexema_reconocido,
            "Error: no es un número válido."
        )




# Pruebas del autómata
if __name__ == "__main__":
    print("  Números NUMBER")
    print("  Escribe salir para terminar.")


    while True:

        cadena_ingresada = input("\n  Ingresa una cadena: ")  # input de cadena a analizar

        if cadena_ingresada == "salir":  # Condición de salida del programa
            break

        es_valido, tipo_token, subtipo, lexema, mensaje = reconocer_numero(cadena_ingresada)

        print(f"  Token    : {tipo_token}  ({subtipo})")
        print(f"  Lexema   : '{lexema}'")
        print(f"  Mensaje  : {mensaje}")
        print("-" * 60)
