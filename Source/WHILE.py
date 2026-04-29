# Token reconocido  : WHILE
# Reconoce la palabra reservada "while". Si la palabra continúa con letras, dígitos o guión bajo después entonces es un NAME.
# "while" es WHILE mientras que "whileloop" es NAME



# Definición de los estados del autómata
ESTADO_INICIAL     = "q0"
ESTADO_VISTO_W     = "q1"   # Leer 'w'
ESTADO_VISTO_WH    = "q2"   # Leer 'wh'
ESTADO_VISTO_WHI   = "q3"   # Leer 'whi'
ESTADO_VISTO_WHIL  = "q4"   # Leer 'whil'
ESTADO_VISTO_WHILE = "q5"   # Leer 'while' es la keyword WHILE
ESTADO_NOMBRE      = "qn"   # El lexema es un identificador (NAME)



# Funciones auxiliares para los caracteres individuales <-----------------------------------

def es_letra(caracter):  # Comprobar si la letra es minúscula o mayúscula
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')


def es_digito(caracter):  # Verificar si es un dígito entre 0 y 9
    return '0' <= caracter <= '9'


def es_guion_bajo(caracter):
    return caracter == '_'


def puede_continuar_identificador(caracter):  # Si este caracter sigue al keyword entonces el token pasa a ser NAME
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)




# ---------------------------------- Función principal para ejecutar el autómata sobre la entrada ----------------------------------

def reconocer_while(cadena_de_entrada):
    
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

            if caracter_actual == 'w':
                estado_actual     = ESTADO_VISTO_W
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE  # Inicia con otra letra: es identificador
                lexema_reconocido += caracter_actual

            else:
                return (False, "ERROR", caracter_actual,
                        f"Error: '{caracter_actual}' no es un carácter de inicio válido.")



        # Loop desde ESTADO_VISTO_W (q1) leímos 'w' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_W:

            if caracter_actual == 'h':
                estado_actual     = ESTADO_VISTO_WH
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'w' sola es NAME



        # Loop desde ESTADO_VISTO_WH (q2) leímos 'wh' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_WH:

            if caracter_actual == 'i':
                estado_actual     = ESTADO_VISTO_WHI
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'wh' sola es NAME



        # Loop desde ESTADO_VISTO_WHI (q3) leímos 'whi' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_WHI:

            if caracter_actual == 'l':
                estado_actual     = ESTADO_VISTO_WHIL
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'whi' sola es NAME



        # Loop desde ESTADO_VISTO_WHIL (q4) leímos 'whil' <--------------------------------------------------------
        elif estado_actual == ESTADO_VISTO_WHIL:

            if caracter_actual == 'e':
                estado_actual     = ESTADO_VISTO_WHILE
                lexema_reconocido += caracter_actual

            elif puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE
                lexema_reconocido += caracter_actual

            else:
                break  # 'whil' sola es NAME



        # Loop desde ESTADO_VISTO_WHILE (q5) leímos 'while' <--------------------------------------------------------
        # Aquí vemos si es keyword o sigue siendo un identificador más largo
        elif estado_actual == ESTADO_VISTO_WHILE:

            if puede_continuar_identificador(caracter_actual):
                estado_actual     = ESTADO_NOMBRE  # por ejemplo "whileloop" es NAME
                lexema_reconocido += caracter_actual

            else:
                break  # El keyword WHILE se reconoció 



        # Loop en ESTADO_NOMBRE (qn) seguimos leyendo el identificador <--------------------------------------------------------
        elif estado_actual == ESTADO_NOMBRE:

            if puede_continuar_identificador(caracter_actual):
                lexema_reconocido += caracter_actual
            else:
                break  # El identificador terminó



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->



    # Regresar el estado final del autómata # <--------------------------------------------------------

    if estado_actual == ESTADO_VISTO_WHILE:
        return (True,  "WHILE", lexema_reconocido, "Keyword 'while' reconocida.")

    elif estado_actual in [ESTADO_NOMBRE, ESTADO_VISTO_W,  ESTADO_VISTO_WH, ESTADO_VISTO_WHI, ESTADO_VISTO_WHIL]:
        return (False, "NAME",  lexema_reconocido, "Identificador reconocido (no es keyword).")

    else:
        return (False, "ERROR", lexema_reconocido, "Error: token no reconocido.")





# Pruebas del autómata
print("  Keyword WHILE")
print("  Escribe 'salir' para terminar.")

while True:

    cadena_ingresada = input("\n  Ingresa una cadena: ")  # input de cadena a analizar

    if cadena_ingresada == "salir":  # Condición de salida del programa
        print("  Programa terminado.")
        break

    es_keyword, tipo_token, lexema, mensaje = reconocer_while(cadena_ingresada)

    print(f"  Token    : {tipo_token}")
    print(f"  Lexema   : '{lexema}'")
    print(f"  Mensaje  : {mensaje}")
    print("-" * 60)
