# Tokens reconocidos: FOR, IN, IS, AND, OR, NOT
# Tipo de implementación: REGEX
#
#  Las keywords se programan comparando la cadena de entrada letra por letra contra cada keyword esperado. Si coincide exactamente y
#  no continúa con caracteres entonces se acepta como keyword. Si continúa con más caracteres entonces el token es NAME (identificador).
#
#   RE para FOR  →  f o r  (seguido de no-alfanumérico)
#   RE para IN   →  i n
#   RE para IS   →  i s
#   RE para AND  →  a n d
#   RE para OR   →  o r
#   RE para NOT  →  n o t


# Funciones auxiliares para los caracteres individuales <-----------------------------------

def es_letra(caracter):  # Comprobar si la letra es minúscula o mayúscula
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')


def es_digito(caracter):  # Verificar si es un dígito entre 0 y 9
    return '0' <= caracter <= '9'


def es_guion_bajo(caracter):
    return caracter == '_'


def puede_continuar_identificador(caracter):  # Si este caracter sigue al keyword, el token pasa a ser NAME
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)




# Función auxiliar compartida que es común para todos los keywords

def comparar_keyword(cadena_de_entrada, keyword_esperado, nombre_token):

    # Parámetros: cadena_de_entrada (str): La cadena que se desea analizar. keyword_esperado  (str): El keyword a comparar (ej. "for", "and").
    # nombre_token      (str): El nombre del token (ej. "FOR", "AND").

    # Retorna tuple: (es_keyword, tipo_token, lexema_reconocido, mensaje_resultado)
    

    longitud_keyword = len(keyword_esperado)
    longitud_entrada = len(cadena_de_entrada)

    lexema_reconocido = ""  # String para ir guardando el texto introducido

    indice_caracter = 0  # Índice para ver en qué caracter estamos



    # ------------------------------------------------------->  LEER LA CADENA CARACTER POR CARACTER <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->


    while indice_caracter < longitud_entrada:  # Bucle para recorrer el input

        caracter_actual  = cadena_de_entrada[indice_caracter]   # Caracter de la entrada en posición actual
        lexema_reconocido += caracter_actual



        # Verificar si aún estamos comparando contra el keyword <--------------------------------------------------------
        if indice_caracter < longitud_keyword:

            caracter_keyword = keyword_esperado[indice_caracter]  # Caracter esperado en esta posición

            if caracter_actual != caracter_keyword:
                # El caracter no coincide con el keyword entonces puede ser NAME u otro token
                if puede_continuar_identificador(caracter_actual):
                    # Seguimos leyendo hasta terminar el identificador
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



        # Ya comparamos todos los caracteres del keyword <--------------------------------------------------------
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
                break  # El keyword terminó limpiamente



        indice_caracter += 1  # Se mueve al siguiente carácter aumentando el índice

    # <---------------------------------------------------------------------------------------------------------------------------->
    # <---------------------------------------------------------------------------------------------------------------------------->



    # Regresar el estado final del autómata # <--------------------------------------------------------

    # Vemos que hayamos leído exactamente todos los caracteres del keyword
    if lexema_reconocido == keyword_esperado:
        return (True, nombre_token, lexema_reconocido, f"Keyword '{keyword_esperado}' reconocida.")

    elif len(lexema_reconocido) > 0 and puede_continuar_identificador(lexema_reconocido[-1]):
        return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")

    else:
        return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")





# Funciones individuales por keyword — cada una llama a comparar_keyword
def reconocer_for(cadena_de_entrada):  # RE para f o r
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "for", "FOR")


def reconocer_in(cadena_de_entrada):   # RE para i n
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "in", "IN")


def reconocer_is(cadena_de_entrada):   # RE para i s
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "is", "IS")


def reconocer_and(cadena_de_entrada):  # RE para a n d
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "and", "AND")


def reconocer_or(cadena_de_entrada):   # RE para o r
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "or", "OR")


def reconocer_not(cadena_de_entrada):  # RE para n o t
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "not", "NOT")





# Diccionario para guardar cada letra inicial al keyword que le toca

# Agrupamos los keywords por su letra inicial para saber cuál función llamar
KEYWORDS_POR_INICIO = {
    'f': reconocer_for,
    'i': None,   # Puede ser IN o IS y se decide con la segunda letra
    'a': reconocer_and,
    'o': reconocer_or,
    'n': reconocer_not,
}

# Para los keywords que inician con 'i' necesitamos revisar su segunda letra
KEYWORDS_CON_I = {
    'n': reconocer_in,
    's': reconocer_is,
}





# Función para detectar automáticamente cuál keyword intentar

def reconocer_keyword_regex(cadena_de_entrada):
    
    # Detecta automáticamente qué keyword intenta ser la cadena y llama a la función que haga falta.
    # Si la cadena no empieza con ninguna letra inicial de keyword conocido intenta reconocerla como NAME (identificador).

    # Regresa tuple: (es_keyword, tipo_token, lexema_reconocido, mensaje_resultado)
    

    if len(cadena_de_entrada) == 0:  # Descartar entradas vacías para iniciar
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    primera_letra = cadena_de_entrada[0]  # Revisamos la primera letra para saber qué keyword intentar

    if primera_letra == 'i' and len(cadena_de_entrada) >= 2:
        # 'i' puede ser IN o IS así que hay que ver la segunda letra decide cuál función usar
        segunda_letra = cadena_de_entrada[1]
        funcion_reconocedora = KEYWORDS_CON_I.get(segunda_letra, None)

        if funcion_reconocedora is not None:
            return funcion_reconocedora(cadena_de_entrada)

    elif primera_letra in KEYWORDS_POR_INICIO and KEYWORDS_POR_INICIO[primera_letra] is not None:
        funcion_reconocedora = KEYWORDS_POR_INICIO[primera_letra]  # Obtenemos la función correcta
        return funcion_reconocedora(cadena_de_entrada)

    # Si no coincide con ningún keyword conocido, es un identificador o error
    if puede_continuar_identificador(primera_letra):
        return (False, "NAME", cadena_de_entrada, "Identificador reconocido (no es keyword de este caso).")

    return (False, "ERROR", cadena_de_entrada, f"Error: '{cadena_de_entrada}' no es un token reconocido.")




# Pruebas de las regex
print("  Tokens regex: FOR  IN  IS  AND  OR  NOT")
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
