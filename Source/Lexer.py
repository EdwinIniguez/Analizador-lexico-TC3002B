import os

import COMPOUND_ASSIGNMENT_OPERATORS
import RELATIONAL_OPERATORS
import SPECIAL_SYMBOLS
import DELIMITERS
import INDENTATION
import OPERATORS
import NAME
import IF_ELSE_ELIF
import DEF_RETURN
import WHILE
import TRUE_FALSE_NONE_PASS_BREAK_CONTINUE
import NUMBER
import STRING
import FOR_IN_IS_AND_OR_NOT


def analizar_codigo_fuente(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        return

    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    INDENTATION.resetear_pila()
    secuencia_tokens = []
    tabla_simbolos = set()  # set para guardar los identificadores unicos

    print("\n" + "="*65)
    print(f"{'TOKEN':<20} | {'LEXEMA':<25} | {'LÍNEA'}")
    print("="*65)

    for num_linea, linea in enumerate(lineas, start=1):
        
        #Pasar la linea completa al automata de indentacion
        tokens_indentacion = INDENTATION.analizar_indentacion(linea)
        
        for token_tuple in tokens_indentacion:
            es_valido, tipo_token, lexema, mensaje = token_tuple
            
            # Manejar los tokens estructurales (INDENT, DEDENT, NEWLINE)
            if tipo_token in ["INDENT", "DEDENT", "NEWLINE"]:
                secuencia_tokens.append((tipo_token, lexema, num_linea))
                # Limpia el salto de linea para imprimir en consola
                lex_print = lexema.replace('\n', '\\n') if lexema else ''
                print(f"{tipo_token:<20} | {lex_print:<25} | {num_linea}")
            
            # Manejar el contenido real de la linea
            elif tipo_token == "TEXTO":
                subcadena = lexema
                indice = 0
                longitud = len(subcadena)
                
                while indice < longitud:
                    # Omitir espacios en blanco y tabuladores internos entre tokens
                    if subcadena[indice] in [' ', '\t', '\n', '\r']:
                        indice += 1
                        continue
                    
                    cadena_actual = subcadena[indice:]
                    match_encontrado = None
                    
                    #STRINGS
                    valido, tipo, lex, msg = STRING.reconocer_cadena(cadena_actual)
                    if valido: 
                        match_encontrado = (tipo, lex)
                    
                    #NUMEROS
                    if not match_encontrado:
                        valido, tipo, subtipo, lex, msg = NUMBER.reconocer_numero(cadena_actual)
                        if valido: 
                            match_encontrado = (tipo, lex)
                    
                    #KEYWORDS
                    if not match_encontrado:
                        valido, tipo, lex, msg = NAME.reconocer_identificador(cadena_actual)
                        if valido:
                            es_keyword = False
                            # Probar contra todos los automatas de keywords
                            para_probar = [
                                IF_ELSE_ELIF.reconocer_condicional,
                                DEF_RETURN.reconocer_keyword_regex,
                                WHILE.reconocer_while,
                                TRUE_FALSE_NONE_PASS_BREAK_CONTINUE.reconocer_keyword_regex,
                                FOR_IN_IS_AND_OR_NOT.reconocer_keyword_regex
                            ]
                            for funcion_kw in para_probar:
                                res_kw = funcion_kw(lex)
                                if res_kw[0]: # es una keyword valida
                                    match_encontrado = (res_kw[1], res_kw[2])
                                    es_keyword = True
                                    break
                            
                            # Si no fue keyword entonces asumimos que es un NAME
                            if not es_keyword:
                                match_encontrado = ("NAME", lex)
                                tabla_simbolos.add(lex) # Añadir a la tabla de simbolos
                    
                    # OPERADORES DE ASIGNACION COMPUESTA (+=, -=, etc.)
                    if not match_encontrado:
                        res = COMPOUND_ASSIGNMENT_OPERATORS.reconocer_operadores_asignacion_compuesta(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # SIMBOLOS ESPECIALES Y DELIMITADORES COMPUESTOS (->, <<, >>, etc.)
                    if not match_encontrado:
                        res = SPECIAL_SYMBOLS.reconocer_simbolo_especial(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # OPERADORES RELACIONALES Y ASIGNACION NORMAL (<=, ==, <, =)
                    if not match_encontrado:
                        res = RELATIONAL_OPERATORS.reconocer_operadores_relacionales_regex(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # DELIMITADORES SIMPLES ( (, [, { )
                    if not match_encontrado:
                        res = DELIMITERS.reconocer_delimitador(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # OPERADORES ARITMETICOS (+, -, *, /, //, %)
                    if not match_encontrado:
                        res = OPERATORS.reconocer_operador_aritmetico(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # RESULTADO DE LA EVALUACIÓN
                    if match_encontrado:
                        tipo_final, lexema_final = match_encontrado
                        secuencia_tokens.append((tipo_final, lexema_final, num_linea))
                        print(f"{tipo_final:<20} | {lexema_final:<25} | {num_linea}")
                        indice += len(lexema_final)
                    else:
                        char_error = subcadena[indice]
                        print(f"{'ERROR':<20} | {char_error:<25} | {num_linea} -> Caracter léxico no reconocido")
                        secuencia_tokens.append(("ERROR", char_error, num_linea))
                        indice += 1

    print("="*65)
    
    # tabla de simbolos
    print("\n" + "="*45)
    print("    TABLA DE SÍMBOLOS (Identificadores)")
    print("="*45)
    for i, simbolo in enumerate(sorted(tabla_simbolos), start=1):
        print(f" ID: {i:03d} | NAME: {simbolo}")
    print("="*45 + "\n")
    
    return secuencia_tokens, tabla_simbolos


if __name__ == '__main__':
    # Archivo de código fuente por defecto
    archivo_prueba = "test_triton.py"
    
    if not os.path.exists(archivo_prueba):
        with open(archivo_prueba, "w", encoding="utf-8") as file:
            file.write("@mi_decorador\n")
            file.write("def prueba_triton(x, y) -> True:\n")
            file.write("    if x == 10:\n")
            file.write("        pass\n")
            file.write("    elif x != 20:\n")
            file.write("        continue\n")
            file.write("    else:\n")
            file.write("        break\n")
            file.write("    while x < 5:\n")
            file.write("        return False\n")
            file.write("    for i in [1, 2, 3]:\n")
            file.write("        a = 1 + 2 - 3 * 4 / 5 // 6 % 7 ** 8\n")
            file.write("        a += 1\n")
            file.write("        a -= 2\n")
            file.write("        a *= 3\n")
            file.write("        a /= 4\n")
            file.write("        b = (a <= 10) and (a >= 5) or not (a > 15) is True\n")
            file.write('        diccionario = {"llave": "valor_string"}\n')
            file.write("        objeto.metodo(x, y)\n")
            file.write("        c = ~a & b ` c ^ d << 1 >> 2\n")
            file.write("    return None\n")
    
    print(f"Iniciando analizador léxico con el archivo de prueba: {archivo_prueba}")
    analizar_codigo_fuente(archivo_prueba)