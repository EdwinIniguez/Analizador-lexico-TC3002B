import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import IF_ELSE_ELIF as lexer  # type: ignore

class TestIfElseElif(unittest.TestCase):

    def test_reconocimiento_exacto(self):
        """Comprueba que los keywords 'if', 'elif' y 'else' sean reconocidos perfectamente."""
        casos = [
            ("if", "IF"),
            ("elif", "ELIF"),
            ("else", "ELSE")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_condicional(entrada)
                self.assertTrue(es_kw)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    def test_prefijos_identificadores(self):
        """Comprueba que identificadores que inician con 'if', 'el' o 'else' sean marcados como NAME."""
        casos = ["iffy", "elephant", "elsewhere", "if1", "elif_var"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_condicional(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    def test_entradas_invalidas(self):
        """Comprueba que arroje un error si le pasamos palabras que no empiezan como condicionales."""
        casos = ["", "a", "x", "xyz"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_condicional(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()