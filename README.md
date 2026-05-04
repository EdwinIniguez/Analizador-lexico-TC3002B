# Analizador Léxico - Triton GPU

## Descripción
Este proyecto implementa la fase de análisis léxico (Scanner) para un compilador del lenguaje Triton GPU, un lenguaje de dominio específico (DSL) similar a Python. El analizador se encarga de procesar el código fuente, identificar los lexemas válidos y generar los tokens correspondientes siguiendo la especificación léxica requerida.

## Características Principales
- Reconocimiento de palabras reservadas, identificadores, números y cadenas de texto.
- Identificación de operadores relacionales, aritméticos y de asignación.
- Procesamiento de delimitadores y símbolos especiales.
- Manejo del control de indentación de Python (NEWLINE, INDENT, DEDENT) mediante un autómata con pila.
- Generación de una secuencia de tokens detallada indicando el tipo, lexema y línea.
- Construcción y exportación de una Tabla de Símbolos para los identificadores únicos.

## Uso
Para ejecutar el analizador léxico, inicia el archivo principal u orquestador del proyecto:

```bash
python Source/Lexer.py
```

Al ejecutarse, el programa procesará el archivo de código fuente de prueba (`test_triton.py`), imprimirá en la consola el desglose secuencial de todos los tokens encontrados y, al finalizar, mostrará la tabla de símbolos generada.
