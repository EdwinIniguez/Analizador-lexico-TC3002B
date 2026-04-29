# Token reconocido  : NAME
# Un identificador válido debe iniciar con una letra (a-z, A-Z) o guión
# bajo (_), y puede continuar con letras, dígitos o guiones bajos.


# Definición de los estados del autómata
ESTADO_INICIAL = "q0"
ESTADO_VALIDO  = "q1"   # Estado válido para nombre
ESTADO_ERROR   = "qe"



# Funciones auxiliares para los caracteres individuales <-----------------------------------

def es_letra(caracter):  # Comprobar si la letra es minúscula o mayúscula
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')


def es_digito(caracter):  # Verificar si es un dígito entre 0 y 9
    return '0' <= caracter <= '9'


def es_guion_bajo(caracter):
    return caracter == '_'


def puede_iniciar_identificador(caracter):  # Solo permitir letra o _ en la primer posición
    return es_letra(caracter) or es_guion_bajo(caracter)


def puede_continuar_identificador(caracter):  # Verificar si se puede usar el caracter para continuar
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)




# ---------------------------------- Función principal para ejecutar el autómata sobre la entrada ----------------------------------

def reconocer_identificador(cadena_de_entrada):
   

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
        if estado_actual == ESTADO_INICIAL:  # Recordar que siempre empezamos en q0 como en los diagramas de las clases

            if puede_iniciar_identificador(caracter_actual):  # Uso la función de arriba para comenzar
                # q0 -- letra o _ --> q1
                estado_actual     = ESTADO_VALIDO  # q1
                lexema_reconocido += caracter_actual

            else:  # Si el estado q0 empieza con dígito u otra cosa no cambia de estado
                estado_actual     = ESTADO_ERROR
                lexema_reconocido += caracter_actual



        # Loop desde el ESTADO VÁLIDO (q1) <--------------------------------------------------------
        elif estado_actual == ESTADO_VALIDO:

            if puede_continuar_identificador(caracter_actual):  # Función de más arriba para ver si podemos seguir llenando el string
                # q1 --> letra, dígito o _ --> q1  se queda loopeando en q1
                lexema_reconocido += caracter_actual

            else:  # Se rompe si el caracter no es válido o si el caracter ya lo leímos
                break



        # Loop cuando está en ESTADO DE ERROR (qe) <--------------------------------------------------------
        elif estado_actual == ESTADO_ERROR:
            break



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->



    # Regresar el estado final del autómata # <--------------------------------------------------------

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
