import unittest
import sys
import os
import tempfile
from io import StringIO
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import Lexer as lexer_principal  # type: ignore

class TestLexer(unittest.TestCase):

    def setUp(self):
        # directorio temporal para escribir archivos de prueba
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Limpiar el directorio temporal
        self.test_dir.cleanup()

    # Crea archivo temporal para las pruebas
    def crear_archivo_temp(self, contenido, nombre="temp.py"):
        ruta = os.path.join(self.test_dir.name, nombre)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        return ruta

    # Primer test
    # 
    def test_analisis_codigo_valido(self):
        """Prueba que el lexer analice correctamente un bloque de código válido y agrupe las estructuras."""
        codigo = "def suma(a, b):\n    return a + b\n"
        ruta = self.crear_archivo_temp(codigo)

        tokens, tabla = lexer_principal.analizar_codigo_fuente(ruta)
        
        # Verifica que se hayan generado tokens
        self.assertIsNotNone(tokens)
        tipos_tokens = [t[0] for t in tokens]
        
        # Valida algunos tokens esperados en esa cadena de texto
        self.assertIn("DEF", tipos_tokens)
        self.assertIn("NAME", tipos_tokens)
        self.assertIn("LPAREN", tipos_tokens)
        self.assertIn("RPAREN", tipos_tokens)
        self.assertIn("COLON", tipos_tokens)
        self.assertIn("RETURN", tipos_tokens)
        self.assertIn("PLUS", tipos_tokens)
        self.assertIn("INDENT", tipos_tokens)

        # Verifica que la tabla de símbolos haya registrado las variables y funciones
        self.assertIn("suma", tabla)
        self.assertIn("a", tabla)
        self.assertIn("b", tabla)

    @patch('sys.stdout', new_callable=StringIO)
    def test_caracter_invalido_generacion_error(self, mock_stdout):
        """PRUEBA NEGATIVA: Verifica que un caracter no reconocido genere un ERROR en tokens y consola."""
        # El caracter '$' no es un símbolo o delimitador válido
        codigo = "variable = 10 $\n"
        ruta = self.crear_archivo_temp(codigo)

        tokens, tabla = lexer_principal.analizar_codigo_fuente(ruta)

        # 1. Validamos que el error está presente en la secuencia generada
        token_error = next(t for t in tokens if t[0] == "ERROR")
        self.assertEqual(token_error[1], "$")  # El lexema del error debe ser '$'
        self.assertEqual(token_error[2], 1)    # Sucedió en la línea 1

        # 2. Validamos el mensaje de error impreso en la consola interceptada
        salida_consola = mock_stdout.getvalue()
        self.assertIn("Caracter léxico no reconocido", salida_consola)
        self.assertIn("$", salida_consola)

    @patch('sys.stdout', new_callable=StringIO)
    def test_archivo_inexistente(self, mock_stdout):
        """PRUEBA NEGATIVA: Verifica cómo se maneja la advertencia cuando el archivo fuente no existe."""
        ruta_falsa = os.path.join(self.test_dir.name, "archivo_fantasma.py")
        resultado = lexer_principal.analizar_codigo_fuente(ruta_falsa)
        
        self.assertIsNone(resultado)
        salida_consola = mock_stdout.getvalue()
        self.assertIn("Error: No se encontró el archivo", salida_consola)

if __name__ == '__main__':
    unittest.main()