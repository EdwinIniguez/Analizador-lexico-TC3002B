# Tokens reconocidos: VERDADERO, FALSO, NONE, PASS, BREAK, CONTINUE
# Tipo de implementación: REGEX
#
#
#   RE para VERDADERO  →  T r u e
#   RE para FALSO      →  F a l s e
#   RE para NONE       →  N o n e  Con N mayúscula
#   RE para PASS       →  p a s s
#   RE para BREAK      →  b r e a k
#   RE para CONTINUE   →  c o n t i n u e


# Funciones auxiliares para los caracteres individuales <-----------------------------------

def es_letra(caracter):  # Comprobar si la letra es minúscula o mayúscula
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')


def es_digito(caracter):  # Verificar si es un dígito entre 0 y 9
    return '0' <= caracter <= '9'


def es_guion_bajo(caracter):
    return caracter == '_'


def puede_continuar_identificador(caracter):  # Si este caracter sigue al keyword entonces debe ser NAME
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)




# Función auxiliar compartida que es común para todos los keywords

def comparar_keyword(cadena_de_entrada, keyword_esperado, nombre_token):

    # Parámetros: cadena_de_entrada (str) es la cadena que se desea analizar. keyword_esperado (str): El keyword a comparar como pass o break.
    # nombre_token (str): El nombre del token (ej. "PASS", "BREAK").

    # Retorna tuple: (es_keyword, tipo_token, lexema_reconocido, mensaje_resultado)

    longitud_keyword = len(keyword_esperado)
    longitud_entrada = len(cadena_de_entrada)

    lexema_reconocido = ""  # String para ir guardando el texto introducido

    indice_caracter = 0  # Índice para ver en qué caracter estamos



    # ------------------------------------------------------->  LEER LA CADENA CARACTER POR CARACTER <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    while indice_caracter < longitud_entrada:  # Bucle para recorrer el input

        caracter_actual   = cadena_de_entrada[indice_caracter]  # Caracter de la entrada en posición actual
        lexema_reconocido += caracter_actual



        # Verificar si aún estamos comparando contra el keyword <--------------------------------------------------------
        if indice_caracter < longitud_keyword:

            caracter_keyword = keyword_esperado[indice_caracter]  # Caracter esperado en esta posición

            if caracter_actual != caracter_keyword:
                # El caracter no coincide con el keyword entonces puede ser NAME u otro token
                if puede_continuar_identificador(caracter_actual):
                    # Seguir leyendo hasta terminar el identificador
                    indice_caracter += 1

                    while indice_caracter < longitud_entrada:
                        siguiente = cadena_de_entrada[indice_caracter]

                        if puede_continuar_identificador(siguiente):
                            lexema_reconocido += siguiente
                        else:
                            break

                        indice_caracter += 1

                    return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")

                else:
                    return (False, "ERROR", lexema_reconocido,
                            f"Error: '{lexema_reconocido}' no es un token reconocido.")



        # Ya terminamos de comparar los caracteres del keyword <--------------------------------------------------------
        elif indice_caracter == longitud_keyword:

            if puede_continuar_identificador(caracter_actual):
                # El keyword continúa con más letras es NAME
                indice_caracter += 1

                while indice_caracter < longitud_entrada:
                    siguiente = cadena_de_entrada[indice_caracter]

                    if puede_continuar_identificador(siguiente):
                        lexema_reconocido += siguiente
                    else:
                        break

                    indice_caracter += 1

                return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")

            else:
                break  # El keyword terminó bien



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    # Vemos que hayamos leído exactamente todos los caracteres del keyword
    if lexema_reconocido == keyword_esperado:
        return (True, nombre_token, lexema_reconocido, f"Keyword '{keyword_esperado}' reconocida.")

    elif len(lexema_reconocido) > 0 and puede_continuar_identificador(lexema_reconocido[-1]):
        return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")

    else:
        return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")




# Funciones individuales por keyword, cada una llama a comparar_keyword
def reconocer_verdadero(cadena_de_entrada):  # RE para V E R D A D E R O
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "True", "VERDADERO")


def reconocer_falso(cadena_de_entrada):      # RE para F A L S O
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "False", "FALSO")


def reconocer_none(cadena_de_entrada):       # RE para N o n e  (N mayúscula)
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "None", "NONE")


def reconocer_pass(cadena_de_entrada):       # RE para p a s s
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "pass", "PASS")


def reconocer_break(cadena_de_entrada):      # RE para b r e a k
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "break", "BREAK")


def reconocer_continue(cadena_de_entrada):   # RE para c o n t i n u e
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "continue", "CONTINUE")




# Diccionario para guardar cada letra inicial al keyword que le toca
# Agrupamos los keywords por su letra inicial para saber cuál función llamar
KEYWORDS_POR_INICIO = {
    'T': reconocer_verdadero,
    'F': reconocer_falso,
    'N': reconocer_none,
    'p': reconocer_pass,
    'b': reconocer_break,
    'c': reconocer_continue,
}




# Función para detectar cuál keyword intentar

def reconocer_keyword_regex(cadena_de_entrada):

    # Detecta automáticamente qué keyword intenta ser la cadena y llama a la función que haga falta.
    # Si la cadena no empieza con ninguna letra inicial de keyword conocido intenta reconocerla como NAME.

    # Regresa tuple: (es_keyword, tipo_token, lexema_reconocido, mensaje_resultado)

    if len(cadena_de_entrada) == 0:  # Descartar entradas vacías para iniciar
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    primera_letra = cadena_de_entrada[0]  # Revisamos la primera letra para saber qué keyword intentar

    if primera_letra in KEYWORDS_POR_INICIO:
        funcion_reconocedora = KEYWORDS_POR_INICIO[primera_letra]  # Obtenemos la función correcta
        return funcion_reconocedora(cadena_de_entrada)

    # Si no coincide con ningún keyword conocido, es un identificador o error
    if puede_continuar_identificador(primera_letra):
        return (False, "NAME", cadena_de_entrada, "Identificador reconocido (no es keyword de este caso).")

    return (False, "ERROR", cadena_de_entrada, f"Error: '{cadena_de_entrada}' no es un token reconocido.")




# Pruebas de las regex
if __name__ == "__main__":
    print("  Tokens regex: VERDADERO  FALSO  NONE  PASS  BREAK  CONTINUE")
    print("  Escribe 'salir' para terminar.")

    while True:

        cadena_ingresada = input("\n  Ingresa una cadena: ")  # input de cadena a analizar

        if cadena_ingresada == "salir":  # Condición de salida del programa
            print("  Programa terminado.")
            break

        es_keyword, tipo_token, lexema, mensaje = reconocer_keyword_regex(cadena_ingresada)

        print(f"  Token    : {tipo_token}")
        print(f"  Lexema   : '{lexema}'")
        print(f"  Mensaje  : {mensaje}")
        print("-" * 60)
