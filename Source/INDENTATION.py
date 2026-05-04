# Tokens: NEWLINE, INDENT, DEDENT
# Implementacion: AUTOMATA CON PILA

pila_indentacion = [0]

# Funcion principal para indentacion

def analizar_indentacion(cadena_de_entrada):

    tokens_generados = []

    if len(cadena_de_entrada) == 0:
        return [(True, "NEWLINE", "\\n", "Salto de línea (línea vacía).")]

    espacios = 0
    indice_caracter = 0

    # Leer espacios iniciales
    while indice_caracter < len(cadena_de_entrada):

        caracter_actual = cadena_de_entrada[indice_caracter]
        
        if caracter_actual == ' ':
            espacios += 1
        elif caracter_actual == '\t':
            espacios += 4
        else:
            break
            
        indice_caracter += 1

    lexema_indentacion = cadena_de_entrada[:indice_caracter]
    contenido_linea    = cadena_de_entrada[indice_caracter:]

    # Evaluar niveles
    nivel_actual = pila_indentacion[-1]

    if espacios > nivel_actual:
        pila_indentacion.append(espacios)
        tokens_generados.append((True, "INDENT", lexema_indentacion, f"Aumento de indentación a {espacios} espacios."))

    elif espacios < nivel_actual:
        while len(pila_indentacion) > 1 and pila_indentacion[-1] > espacios:
            pila_indentacion.pop()
            tokens_generados.append((True, "DEDENT", "", f"Reducción de indentación al nivel de {pila_indentacion[-1]} espacios."))
        
        if pila_indentacion[-1] != espacios:
            tokens_generados.append((False, "ERROR", lexema_indentacion, f"Error de Indentación: la reducción de {espacios} espacios no coincide con ningún nivel anterior."))

    # Agregar NEWLINE
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
if __name__ == "__main__":
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