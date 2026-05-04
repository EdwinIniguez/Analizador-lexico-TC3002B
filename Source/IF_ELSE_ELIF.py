# Tokens reconocidos: IF, ELIF, ELSE
# If, Else, elif van juntos en un solo autómata
#
# 
# Reconoce las palabras reservadas "if", "elif" y "else".
# Si la palabra continúa con letras o dígitos después del keyword es un identificador (NAME) y no una keyword.
# "if" → IF , "iffy" → NAME o "else" → ELSE


# Definición de los estados del autómata
ESTADO_INICIAL    = "q0"
ESTADO_VISTO_I    = "q1"    # Leer 'i'
ESTADO_VISTO_IF   = "q2"    # Leer 'if' es una posible keyword IF
ESTADO_VISTO_E    = "q3"    # Leer 'e'
ESTADO_VISTO_EL   = "q4"    # Leer 'el'
ESTADO_VISTO_ELI  = "q5"    # Leer 'eli'
ESTADO_VISTO_ELIF = "q6"    # Leer 'elif' es una posible keyword ELIF
ESTADO_VISTO_ELS  = "q7"    # Leer 'els'
ESTADO_VISTO_ELSE = "q8"    # Leer 'else' es una posible keyword ELSE
ESTADO_NOMBRE     = "qn"    # El input es un identificador (NAME) y no un keyword


# Funciones auxiliares para los caracteres individuales <-----------------------------------

def es_letra(caracter):  # Comprobar si la letra es minúscula o mayúscula
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')


def es_digito(caracter):  # Verificar si es un dígito entre 0 y 9
    return '0' <= caracter <= '9'


def es_guion_bajo(caracter):
    return caracter == '_'


def puede_continuar_identificador(caracter):  # Si este caracter sigue al keyword entonces el token pasa a ser NAME
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)




# Función auxiliar para manejar los estados de posible keyword <-----------------------------------

def transicion_desde_posible_keyword(caracter_actual, lexema_reconocido):
    # Cuando estamos en q2, q6 o q8 (los estados de keywords completas) y llega otro caracter vemos si sigue siendo keyword o pasa a NAME
    if puede_continuar_identificador(caracter_actual):
        return (ESTADO_NOMBRE, lexema_reconocido + caracter_actual)  # Pasa a ser identificador
    else:
        return (None, lexema_reconocido)  # None marca que el keyword fue reconocido en la tupla




# ---------------------------------- Función principal para ejecutar el autómata sobre la entrada ----------------------------------

def reconocer_condicional(cadena_de_entrada):

    # Retorna tuple: (es_keyword, tipo_token, lexema_reconocido, mensaje_resultado)

    if len(cadena_de_entrada) == 0:  # Descartar entradas vacías para iniciar
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

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

            if caracter_actual == 'i':
                estado_actual     = ESTADO_VISTO_I
                lexema_reconocido += caracter_actual

            elif caracter_actual == 'e':
                estado_actual     = ESTADO_VISTO_E
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE  # Inicia con otra letra: es identificador
                lexema_reconocido += caracter_actual

            else:
                return (False, "ERROR", caracter_actual,
                        f"Error: '{caracter_actual}' no es un carácter de inicio válido.")



        # Loop desde ESTADO_VISTO_I (q1): leímos 'i' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_I:

            if caracter_actual == 'f':
                estado_actual     = ESTADO_VISTO_IF
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'i' sola es NAME



        # Loop desde ESTADO_VISTO_IF (q2): leímos 'if' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_IF:

            nuevo_estado, lexema_reconocido = transicion_desde_posible_keyword(caracter_actual, lexema_reconocido)

            if nuevo_estado is None:
                break  # Aceptamos IF como keyword
            else:
                estado_actual = nuevo_estado



        # Loop desde ESTADO_VISTO_E (q3): leímos 'e' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_E:

            if caracter_actual == 'l':
                estado_actual     = ESTADO_VISTO_EL
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'e' sola: es NAME



        # Loop desde ESTADO_VISTO_EL (q4): leímos 'el' <--------------------------------------------------------
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
                break  # 'el' sola es NAME



        # Loop desde ESTADO_VISTO_ELI (q5): leímos 'eli' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_ELI:

            if caracter_actual == 'f':
                estado_actual     = ESTADO_VISTO_ELIF
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'eli' sola es NAME



        # Loop desde ESTADO_VISTO_ELIF (q6): leímos 'elif' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_ELIF:

            nuevo_estado, lexema_reconocido = transicion_desde_posible_keyword(caracter_actual, lexema_reconocido)

            if nuevo_estado is None:
                break  # Aceptamos ELIF como keyword
            else:
                estado_actual = nuevo_estado



        # Loop desde ESTADO_VISTO_ELS (q7): leímos 'els' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_ELS:

            if caracter_actual == 'e':
                estado_actual     = ESTADO_VISTO_ELSE
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'els' sola es NAME



        # Loop desde ESTADO_VISTO_ELSE (q8): leímos 'else' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_ELSE:

            nuevo_estado, lexema_reconocido = transicion_desde_posible_keyword(caracter_actual, lexema_reconocido)

            if nuevo_estado is None:
                break  # Aceptamos ELSE como keyword
            else:
                estado_actual = nuevo_estado



        # Loop en ESTADO_NOMBRE (qn): seguimos leyendo el identificador <--------------------------------------------------------
        elif estado_actual == ESTADO_NOMBRE:

            if puede_continuar_identificador(caracter_actual):
                lexema_reconocido += caracter_actual
            else:
                break  # El identificador terminó



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->



    # Regresar el estado final del autómata # <--------------------------------------------------------

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
