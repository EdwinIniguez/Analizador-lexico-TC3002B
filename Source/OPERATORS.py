# Tokens reconocidos: PLUS (+), MINUS (-), TIMES (*), POWER (**), DIVIDE (/), FLOORDIV (//), MOD (%)
# Algunos operadores son de un solo carácter +, -, % y se aceptan rápido
# Otros necesitan ver el siguiente carácter para decidir '*'  solo es TIMES y '**' es POWER
# '/'  solo es DIVIDE y  '//' es FLOORDIV


# Definición de los estados del autómata
ESTADO_INICIAL      = "q0"
ESTADO_VISTO_STAR   = "q1"   # Leímos '*', esperamos saber si es '*' o '**'
ESTADO_VISTO_SLASH  = "q2"   # Leímos '/', esperamos saber si es '/' o '//'



# Constantes para los caracteres de cada operador <-----------------------------------

CARACTER_SUMA       = '+'
CARACTER_RESTA      = '-'
CARACTER_ESTRELLA   = '*'
CARACTER_DIAGONAL   = '/'
CARACTER_PORCENTAJE = '%'




# ---------------------------------- Función principal para ejecutar el autómata sobre la entrada ----------------------------------

def reconocer_operador_aritmetico(cadena_de_entrada):

    # Retorna tuple: (es_valido, tipo_token, lexema_reconocido, mensaje_resultado)

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

            if caracter_actual == CARACTER_SUMA:
                # q0 --[+]--> ACEPTA PLUS de una vez porque tiene un solo caracter
                lexema_reconocido += caracter_actual
                return (True, "PLUS", lexema_reconocido, "Operador suma reconocido.")

            elif caracter_actual == CARACTER_RESTA:
                # q0 --[-]--> ACEPTA MINUS de una vez porque tiene un solo caracter
                lexema_reconocido += caracter_actual
                return (True, "MINUS", lexema_reconocido, "Operador resta reconocido.")

            elif caracter_actual == CARACTER_PORCENTAJE:
                # q0 --[%]--> ACEPTA MOD de una vez porque tiene un solo caracter
                lexema_reconocido += caracter_actual
                return (True, "MOD", lexema_reconocido, "Operador módulo reconocido.")

            elif caracter_actual == CARACTER_ESTRELLA:
                # q0 --[*]--> q1  hay que verificar si viene otro igual
                estado_actual     = ESTADO_VISTO_STAR
                lexema_reconocido += caracter_actual

            elif caracter_actual == CARACTER_DIAGONAL:
                # q0 --[/]--> q2  hay que verificar si viene otra '/'
                estado_actual     = ESTADO_VISTO_SLASH
                lexema_reconocido += caracter_actual

            else:  # El caracter no es ningún operador 
                return (
                    False,
                    "ERROR",
                    caracter_actual,
                    f"Error léxico: '{caracter_actual}' no es un operador aritmético válido."
                )



        # Loop desde ESTADO_VISTO_STAR (q1): ya leímos un '*' <--------------------------------------------------------
        # Ahora vemos si es TIMES (*) o POWER (**)
        elif estado_actual == ESTADO_VISTO_STAR:

            if caracter_actual == CARACTER_ESTRELLA:
                # q1 --[*]--> acepta POWER  (**)
                lexema_reconocido += caracter_actual
                return (True, "POWER", lexema_reconocido, "Operador potencia reconocido.")

            else:
                # El siguiente caracter no es '*' entonces aceptamos TIMES (*)
                # Ese caracter pertenece al siguiente token, no lo consumimos
                return (True, "TIMES", lexema_reconocido, "Operador multiplicación reconocido.")



        # Loop desde ESTADO_VISTO_SLASH (q2): ya leímos un '/' <--------------------------------------------------------
        # Ahora vemos si es DIVIDE / o FLOORDIV //
        elif estado_actual == ESTADO_VISTO_SLASH:

            if caracter_actual == CARACTER_DIAGONAL:
                # q2 --[/]--> acepta FLOORDIV  (//)
                lexema_reconocido += caracter_actual
                return (True, "FLOORDIV", lexema_reconocido, "Operador división entera reconocido.")

            else:
                # El siguiente caracter no es '/' entonces aceptamos DIVIDE (/)
                # Ese caracter pertenece al siguiente token, no lo consumimos
                return (True, "DIVIDE", lexema_reconocido, "Operador división reconocido.")



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->



    # Regresar el estado final del autómata cuando terminó la cadena sin más caracteres # <--------------------------------------------------------

    if estado_actual == ESTADO_VISTO_STAR:
        return (True, "TIMES", lexema_reconocido, "Operador multiplicación reconocido.")

    elif estado_actual == ESTADO_VISTO_SLASH:
        return (True, "DIVIDE", lexema_reconocido, "Operador división reconocido.")

    else:
        return (False, "ERROR", lexema_reconocido, "Error: no se pudo reconocer el operador.")




# Pruebas del autómata
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
