# Token reconocido  : NUMBER (entero o decimal)
# Un número puede ser entero (42) o decimal (3.14)
# No se acepta un punto sin dígitos después (3. es error).



# Definición de los estados del autómata
ESTADO_INICIAL    = "q0"
ESTADO_ENTERO     = "q1"   # Estado de aceptación para número entero
ESTADO_TRAS_PUNTO = "q2"   # Vimos un punto, esperamos dígito
ESTADO_DECIMAL    = "q3"   # Estado de aceptación para número decimal
ESTADO_ERROR      = "qe"



# Funciones auxiliares para los caracteres individuales <-----------------------------------

def es_digito(caracter):  # Verificar si es un dígito entre 0 y 9
    return '0' <= caracter <= '9'


def es_punto_decimal(caracter):  # Verificar si es el separador decimal
    return caracter == '.'




# ---------------------------------- Función principal para ejecutar el autómata sobre la entrada ----------------------------------

def reconocer_numero(cadena_de_entrada):
    
    # Retorna tuple: (es_valido, tipo_token, lexema_reconocido, mensaje_resultado)

    if len(cadena_de_entrada) == 0:  # Descartar entradas vacías para iniciar
        return (False, "ERROR", "", "", "Error: la cadena de entrada está vacía.")

    # Comenzar en estado inicial
    estado_actual = ESTADO_INICIAL

    lexema_reconocido = ""  # String para ir guardando el texto introducido

    indice_caracter = 0  # Índice para ver en qué caracter estamos



    # ------------------------------------------------------->  LEER LA CADENA CARACTER POR CARACTER <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    while indice_caracter < len(cadena_de_entrada):  # Bucle para recorrer el input

        caracter_actual = cadena_de_entrada[indice_caracter]  # Comenzamos por el caracter en la posición actual



        # Loop desde el ESTADO INICIAL (q0) <--------------------------------------------------------
        if estado_actual == ESTADO_INICIAL:

            if es_digito(caracter_actual):
                # q0 --[dígito]--> q1  leer la parte entera
                estado_actual     = ESTADO_ENTERO
                lexema_reconocido += caracter_actual

            else:  # No puede iniciar un número con punto ni otro caracter
                estado_actual     = ESTADO_ERROR
                lexema_reconocido += caracter_actual



        # Loop desde el ESTADO ENTERO (q1) <--------------------------------------------------------
        elif estado_actual == ESTADO_ENTERO:

            if es_digito(caracter_actual):
                # q1 --[dígito]--> q1  continúa el número entero
                lexema_reconocido += caracter_actual

            elif es_punto_decimal(caracter_actual):
                # q1 --[punto]--> q2 
                estado_actual     = ESTADO_TRAS_PUNTO
                lexema_reconocido += caracter_actual

            else:  # El caracter no forma parte del número
                break



        # Loop desde el ESTADO TRAS PUNTO (q2) <--------------------------------------------------------
        elif estado_actual == ESTADO_TRAS_PUNTO:

            if es_digito(caracter_actual):
                # q2 --[dígito]--> q3  parte de fracción después del punto
                estado_actual     = ESTADO_DECIMAL
                lexema_reconocido += caracter_actual

            else:  # El punto no fue seguido de dígito y es error
                estado_actual = ESTADO_ERROR
                break



        # Loop desde el ESTADO DECIMAL (q3) <--------------------------------------------------------
        elif estado_actual == ESTADO_DECIMAL:

            if es_digito(caracter_actual):
                # q3 --[dígito]--> q3  continúa la parte decimal
                lexema_reconocido += caracter_actual

            elif es_punto_decimal(caracter_actual):
                # q3 --[segundo punto]--> qe  doble punto no es válido
                estado_actual = ESTADO_ERROR
                break

            else:  # El caracter no forma parte del decimal
                break



        # Loop cuando está en ESTADO DE ERROR (qe) <--------------------------------------------------------
        elif estado_actual == ESTADO_ERROR:
            break



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->



    # Regresar el estado final del autómata # <--------------------------------------------------------

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
