# Token reconocido  : STRING
#  Una cadena válida inicia con comilla doble ("), contiene cualquier
#  carácter excepto comilla o salto de línea, y cierra con comilla doble.
#  Una cadena que no cierra antes del salto de línea es error.



# Definición de los estados del autómata
ESTADO_INICIAL       = "q0"
ESTADO_LEYENDO       = "q1"   # Dentro de la cadena leyendo su contenido
ESTADO_CADENA_CIERRA = "q2"   # Estado de aceptación (comilla de cierre vista)
ESTADO_ERROR         = "qe"



# Constantes para los caracteres especiales <-----------------------------------

COMILLA_DOBLE  = '"'
SALTO_DE_LINEA = '\n'




# ---------------------------------- Función principal para ejecutar el autómata sobre la entrada ----------------------------------

def reconocer_cadena(cadena_de_entrada):

    # Retorna tuple: (es_valido, tipo_token, lexema_reconocido, mensaje_resultado)

    if len(cadena_de_entrada) == 0:  # Descartar entradas vacías para iniciar
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    # Comenzar en estado inicial
    estado_actual = ESTADO_INICIAL

    lexema_reconocido = ""  # String para ir guardando el texto introducido incluyendo las comillas

    indice_caracter = 0  # Índice para ver en qué caracter estamos



    # ------------------------------------------------------->  LEER LA CADENA CARACTER POR CARACTER <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    while indice_caracter < len(cadena_de_entrada):  # Bucle para recorrer el input

        caracter_actual = cadena_de_entrada[indice_caracter]  # Comenzamos por el caracter en la posición actual



        # Loop desde el ESTADO INICIAL (q0) <--------------------------------------------------------
        if estado_actual == ESTADO_INICIAL:

            if caracter_actual == COMILLA_DOBLE:
                # q0 --[comilla doble]--> q1  inicia la cadena
                estado_actual     = ESTADO_LEYENDO
                lexema_reconocido += caracter_actual

            else:  # Una cadena siempre debe iniciar con comilla
                estado_actual     = ESTADO_ERROR
                lexema_reconocido += caracter_actual



        # Loop desde el ESTADO LEYENDO (q1) <--------------------------------------------------------
        elif estado_actual == ESTADO_LEYENDO:

            if caracter_actual == COMILLA_DOBLE:
                # q1 --[comilla doble]--> q2  la cadena se cierra bien
                estado_actual     = ESTADO_CADENA_CIERRA
                lexema_reconocido += caracter_actual
                indice_caracter   += 1  # Avanzamos manualmente porque el token está completo
                break

            elif caracter_actual == SALTO_DE_LINEA:
                # q1 --[salto de línea]--> qe  la cadena no puede tener saltos internos
                estado_actual = ESTADO_ERROR
                break

            else:
                # q1 --[caracter válido]--> q1  seguimos leyendo la cadena
                lexema_reconocido += caracter_actual



        # Loop cuando está en ESTADO DE ERROR (qe) <--------------------------------------------------------
        elif estado_actual == ESTADO_ERROR:
            break



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    if estado_actual == ESTADO_LEYENDO:  # Si terminamos sin cerrar la cadena es error
        estado_actual = ESTADO_ERROR



    # Regresar el estado final del autómata # <--------------------------------------------------------

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
