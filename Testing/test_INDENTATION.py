import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import INDENTATION as lexer  # type: ignore

class TestIndentation(unittest.TestCase):

    def setUp(self):
        """Este método se ejecuta antes de cada prueba. Garantiza que la pila esté limpia."""
        lexer.resetear_pila()

    def test_linea_vacia_sin_indentacion(self):
        """Prueba que una línea vacía devuelva un NEWLINE sin alterar la pila."""
        tokens = lexer.analizar_indentacion("")
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0][1], "NEWLINE")

    def test_aumento_indentacion(self):
        """Prueba que agregar espacios incremente la indentación (INDENT)."""
        tokens = lexer.analizar_indentacion("    x = 1")
        # Debe generar INDENT, TEXTO, y NEWLINE
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0][1], "INDENT")
        self.assertEqual(tokens[0][2], "    ")
        self.assertEqual(tokens[1][1], "TEXTO")
        self.assertEqual(tokens[1][2], "x = 1")
        self.assertEqual(tokens[2][1], "NEWLINE")
        self.assertEqual(lexer.pila_indentacion, [0, 4])

    def test_disminucion_indentacion_simple(self):
        """Prueba que volver a 0 espacios genere un DEDENT."""
        # Pre-llenamos la pila
        lexer.analizar_indentacion("    x = 1")
        
        # Reducimos a 0
        tokens = lexer.analizar_indentacion("y = 2")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0][1], "DEDENT")
        self.assertEqual(lexer.pila_indentacion, [0])

    def test_disminucion_indentacion_multiple(self):
        """Prueba el retroceso de varios niveles de indentación (Ej: de 8 espacios a 0)."""
        lexer.analizar_indentacion("    nivel 1")
        lexer.analizar_indentacion("        nivel 2")
        
        tokens = lexer.analizar_indentacion("z = 3")
        # Debe generar dos DEDENT (del nivel 8 al 4, y del 4 al 0), TEXTO y NEWLINE
        tipos_tokens = [t[1] for t in tokens]
        self.assertEqual(tipos_tokens, ["DEDENT", "DEDENT", "TEXTO", "NEWLINE"])
        self.assertEqual(lexer.pila_indentacion, [0])

    def test_error_indentacion(self):
        """Prueba que niveles de reducción no coincidentes generen un error."""
        lexer.analizar_indentacion("    nivel 1")
        tokens = lexer.analizar_indentacion("  nivel_intermedio")
        self.assertEqual(tokens[1][1], "ERROR")

if __name__ == '__main__':
    unittest.main()