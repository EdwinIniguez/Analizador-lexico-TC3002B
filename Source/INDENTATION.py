# Tokens reconocidos: NEWLINE, INDENT, DEDENT
# Tipo de implementación: AUTÓMATA CON PILA (Stack-based Automaton)
#
# A diferencia de los otros tokens, la indentación en lenguajes como Python no se puede
# evaluar de forma aislada solo viendo un caracter. Se necesita una "pila" (stack) para
# recordar el nivel de indentación actual y compararlo con el de las líneas anteriores.
#
#   NEWLINE → Salto de línea (\n)
#   INDENT  → Aumento en la cantidad de espacios/tabuladores al inicio de una línea.
#   DEDENT  → Disminución en la cantidad de espacios/tabuladores al inicio de una línea.


pila_indentacion = [0]  # Pila global para llevar el registro de los niveles de indentación




# ---------------------------------- Función principal para ejecutar el autómata sobre la entrada ----------------------------------

def analizar_indentacion(cadena_de_entrada):

    # Parámetros: cadena_de_entrada (str): La línea de código a analizar.
    # Retorna una lista de tuplas con el formato: (es_valido, tipo_token, lexema_reconocido, mensaje_resultado)

    tokens_generados = []

    if len(cadena_de_entrada) == 0:
        # En una línea vacía simplemente emitimos un NEWLINE
        return [(True, "NEWLINE", "\\n", "Salto de línea (línea vacía).")]


    espacios = 0
    indice_caracter = 0


    # -------------------------------------------------------> LEER CARACTERES DE INDENTACIÓN <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    while indice_caracter < len(cadena_de_entrada):

        caracter_actual = cadena_de_entrada[indice_caracter]
        
        if caracter_actual == ' ':
            espacios += 1
        elif caracter_actual == '\t':
            espacios += 4  # Un tabulador comúnmente cuenta como 4 espacios
        else:
            break  # Terminó la indentación y comienza el texto
            
        indice_caracter += 1


    lexema_indentacion = cadena_de_entrada[:indice_caracter]
    contenido_linea    = cadena_de_entrada[indice_caracter:]


    # -------------------------------------------------------> EVALUAR LA PILA DE INDENTACIÓN <--------------------------------------------------------
    # <---------------------------------------------------------------------------------------------------------------------------->
    nivel_actual = pila_indentacion[-1]

    if espacios > nivel_actual:
        # Aumento de indentación -> INDENT
        pila_indentacion.append(espacios)
        tokens_generados.append((True, "INDENT", lexema_indentacion, f"Aumento de indentación a {espacios} espacios."))

    elif espacios < nivel_actual:
        # Reducción de indentación -> DEDENT (Puede generar múltiples DEDENTs si retrocede varios niveles)
        while len(pila_indentacion) > 1 and pila_indentacion[-1] > espacios:
            pila_indentacion.pop()
            tokens_generados.append((True, "DEDENT", "", f"Reducción de indentación al nivel de {pila_indentacion[-1]} espacios."))
        
        # Verificar si el nuevo nivel coincide con uno de los niveles existentes en la pila
        if pila_indentacion[-1] != espacios:
            tokens_generados.append((False, "ERROR", lexema_indentacion, f"Error de Indentación: la reducción de {espacios} espacios no coincide con ningún nivel anterior."))


    # -------------------------------------------------------> AGREGAR NEWLINE AL FINAL <--------------------------------------------------------
    # Simulamos que al final de la instrucción leída siempre hay un salto de línea
    if contenido_linea:
        tokens_generados.append((True, "TEXTO", contenido_linea, "Contenido de la línea (otros tokens)."))
        tokens_generados.append((True, "NEWLINE", "\\n", "Salto de línea reconocido al final de la instrucción."))
    else:
        tokens_generados.append((True, "NEWLINE", "\\n", "Salto de línea reconocido."))

    return tokens_generados



def resetear_pila():
    global pila_indentacion
    pila_indentacion = [0]



# Pruebas del autómata con pila
print("  Tokens de control de indentación: NEWLINE, INDENT, DEDENT")
print("  Nota: Agrega espacios al inicio de tu texto para simular la indentación.")
print("  Escribe 'salir' para terminar o 'reset' para vaciar la pila de indentación.")

while True:

    cadena_ingresada = input("\n  Ingresa una línea: ")

    if cadena_ingresada == "salir":
        print("  Programa terminado.")
        break
    elif cadena_ingresada == "reset":
        resetear_pila()
        print("  Pila de indentación reseteada a [0].")
        continue

    lista_tokens = analizar_indentacion(cadena_ingresada)

    for es_valido, tipo_token, lexema, mensaje in lista_tokens:
        print(f"  Token    : {tipo_token:<8} | Lexema: '{lexema}' | {mensaje}")