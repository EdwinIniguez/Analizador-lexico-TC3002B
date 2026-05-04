import os
import sys

# Importación de todos los submódulos del analizador
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
    tabla_simbolos = set()  # Usamos un set para guardar identificadores únicos

    print("\n" + "="*65)
    print(f"{'TOKEN':<20} | {'LEXEMA':<25} | {'LÍNEA'}")
    print("="*65)

    for num_linea, linea in enumerate(lineas, start=1):
        
        # 1. Pasar la línea completa al autómata de indentación
        tokens_indentacion = INDENTATION.analizar_indentacion(linea)
        
        for token_tuple in tokens_indentacion:
            es_valido, tipo_token, lexema, mensaje = token_tuple
            
            # Manejar los tokens estructurales (INDENT, DEDENT, NEWLINE)
            if tipo_token in ["INDENT", "DEDENT", "NEWLINE"]:
                secuencia_tokens.append((tipo_token, lexema, num_linea))
                # Limpiamos el salto de línea para que se imprima explícitamente en consola
                lex_print = lexema.replace('\n', '\\n') if lexema else ''
                print(f"{tipo_token:<20} | {lex_print:<25} | {num_linea}")
            
            # Manejar el contenido real de la línea
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
                    
                    # -- ORDEN DE PRIORIDAD DE EVALUACIÓN --
                    
                    # 1. STRINGS (Cadenas de texto)
                    valido, tipo, lex, msg = STRING.reconocer_cadena(cadena_actual)
                    if valido: 
                        match_encontrado = (tipo, lex)
                    
                    # 2. NÚMEROS
                    if not match_encontrado:
                        valido, tipo, subtipo, lex, msg = NUMBER.reconocer_numero(cadena_actual)
                        if valido: 
                            match_encontrado = (tipo, lex)
                    
                    # 3. IDENTIFICADORES Y KEYWORDS
                    if not match_encontrado:
                        valido, tipo, lex, msg = NAME.reconocer_identificador(cadena_actual)
                        if valido:
                            es_keyword = False
                            # Probar contra todos los autómatas de palabras reservadas
                            para_probar = [
                                IF_ELSE_ELIF.reconocer_condicional,
                                DEF_RETURN.reconocer_keyword_regex,
                                WHILE.reconocer_while,
                                TRUE_FALSE_NONE_PASS_BREAK_CONTINUE.reconocer_keyword_regex,
                                FOR_IN_IS_AND_OR_NOT.reconocer_keyword_regex
                            ]
                            for funcion_kw in para_probar:
                                res_kw = funcion_kw(lex)
                                if res_kw[0]: # Si es una keyword válida
                                    match_encontrado = (res_kw[1], res_kw[2])
                                    es_keyword = True
                                    break
                            
                            # Si no fue keyword, entonces garantizamos que es un NAME
                            if not es_keyword:
                                match_encontrado = ("NAME", lex)
                                tabla_simbolos.add(lex) # Añadir a la tabla de símbolos
                    
                    # 4. OPERADORES DE ASIGNACIÓN COMPUESTA (+=, -=, etc.)
                    if not match_encontrado:
                        res = COMPOUND_ASSIGNMENT_OPERATORS.reconocer_operadores_asignacion_compuesta(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # 5. SÍMBOLOS ESPECIALES Y DELIMITADORES COMPUESTOS (->, <<, >>, etc.)
                    # (Deben ir antes de relacionales y aritméticos para que '->' no se lea como '-')
                    if not match_encontrado:
                        res = SPECIAL_SYMBOLS.reconocer_simbolo_especial(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # 6. OPERADORES RELACIONALES Y ASIGNACIÓN NORMAL (<=, ==, <, =)
                    if not match_encontrado:
                        res = RELATIONAL_OPERATORS.reconocer_operadores_relacionales_regex(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # 7. DELIMITADORES SIMPLES ( (, [, { )
                    if not match_encontrado:
                        res = DELIMITERS.reconocer_delimitador(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # 8. OPERADORES ARITMÉTICOS (+, -, *, /, //, %)
                    if not match_encontrado:
                        res = OPERATORS.reconocer_operador_aritmetico(cadena_actual)
                        if res[0]: match_encontrado = (res[1], res[2])
                        
                    # -- RESULTADO DE LA EVALUACIÓN --
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
    
    # Generar la Tabla de Símbolos Requerida
    print("\n" + "="*45)
    print("    TABLA DE SÍMBOLOS (Identificadores)")
    print("="*45)
    for i, simbolo in enumerate(sorted(tabla_simbolos), start=1):
        print(f" ID: {i:03d} | NAME: {simbolo}")
    print("="*45 + "\n")


if __name__ == '__main__':
    # Archivo de código fuente por defecto (se crea de ejemplo si no existe)
    archivo_prueba = "test_triton.py"
    
    if not os.path.exists(archivo_prueba):
        with open(archivo_prueba, "w", encoding="utf-8") as file:
            file.write("def mi_kernel_triton(x, y):\n")
            file.write("    while x < 10:\n")
            file.write("        if x == 5:\n")
            file.write("            pass\n")
            file.write("        x += 1\n")
            file.write('        nombre = "hola"\n')
            file.write("    return VERDADERO\n")
    
    print(f"Iniciando analizador léxico con el archivo de prueba: {archivo_prueba}")
    analizar_codigo_fuente(archivo_prueba)