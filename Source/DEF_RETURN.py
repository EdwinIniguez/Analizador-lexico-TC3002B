# Tokens: DEF, RETURN
# Implementacion: REGEX

# Funciones auxiliares para caracteres

def es_letra(caracter):
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_guion_bajo(caracter):
    return caracter == '_'

def puede_continuar_identificador(caracter):
    return es_letra(caracter) or es_digito(caracter) or es_guion_bajo(caracter)

# Funcion auxiliar para keywords

def comparar_keyword(cadena_de_entrada, keyword_esperado, nombre_token):

    # Parametros: cadena, keyword y nombre del token
    # Retorna: (es_keyword, tipo, lexema, mensaje)

    longitud_keyword = len(keyword_esperado)
    longitud_entrada = len(cadena_de_entrada)

    lexema_reconocido = ""
    indice_caracter = 0

    # Leer la cadena caracter por caracter

    while indice_caracter < longitud_entrada:

        caracter_actual   = cadena_de_entrada[indice_caracter]
        lexema_reconocido += caracter_actual

        # Verificar coincidencia con keyword
        if indice_caracter < longitud_keyword:

            caracter_keyword = keyword_esperado[indice_caracter]

            if caracter_actual != caracter_keyword:
                # Si no coincide, puede ser un identificador (NAME)
                if puede_continuar_identificador(caracter_actual):
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

        # Keyword completa
        elif indice_caracter == longitud_keyword:

            if puede_continuar_identificador(caracter_actual):
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
                break

        indice_caracter += 1

    # Validar resultado
    if lexema_reconocido == keyword_esperado:
        return (True, nombre_token, lexema_reconocido, f"Keyword '{keyword_esperado}' reconocida.")

    elif len(lexema_reconocido) > 0 and puede_continuar_identificador(lexema_reconocido[-1]):
        return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")

    else:
        return (False, "NAME", lexema_reconocido, "Identificador reconocido (no es keyword).")




# Funciones individuales por keyword, cada una llama a comparar_keyword
def reconocer_def(cadena_de_entrada):     # RE para d e f
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "def", "DEF")


def reconocer_return(cadena_de_entrada):  # RE para r e t u r n
    if len(cadena_de_entrada) == 0:
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")
    return comparar_keyword(cadena_de_entrada, "return", "RETURN")




# Diccionario para guardar cada letra inicial al keyword que le toca

# DEF y RETURN inician con letras diferentes así que el diccionario es más simple
KEYWORDS_POR_INICIO = {
    'd': reconocer_def,
    'r': reconocer_return,
}




# Función para detectar automáticamente cuál keyword intentar

def reconocer_keyword_regex(cadena_de_entrada):

    # Detecta automáticamente qué keyword intenta ser la cadena y llama a la función que haga falta.
    # Si la cadena no empieza con ninguna letra inicial de keyword conocido intenta reconocerla como NAME (identificador)

    # Regresa tuple: (es_keyword, tipo_token, lexema_reconocido, mensaje_resultado)

    if len(cadena_de_entrada) == 0:  # Descartar entradas vacías para iniciar
        return (False, "ERROR", "", "Error: la cadena de entrada está vacía.")

    primera_letra = cadena_de_entrada[0]  # Revisamos la primera letra para saber qué keyword intentar

    if primera_letra in KEYWORDS_POR_INICIO:
        funcion_reconocedora = KEYWORDS_POR_INICIO[primera_letra]  # Obtenemos la función correcta
        return funcion_reconocedora(cadena_de_entrada)

    # Si no coincide con ningún keyword conocido entonces es un identificador o error
    if puede_continuar_identificador(primera_letra):
        return (False, "NAME", cadena_de_entrada, "Identificador reconocido (no es keyword de este caso).")

    return (False, "ERROR", cadena_de_entrada, f"Error: '{cadena_de_entrada}' no es un token reconocido.")




# Pruebas de las regex
if __name__ == "__main__":
    print("  Tokens regex: DEF  RETURN")
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
