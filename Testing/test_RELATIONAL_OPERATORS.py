import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import RELATIONAL_OPERATORS as lexer  # type: ignore

class TestRelationalOperators(unittest.TestCase):

    def test_operadores_simples(self):
        """Comprueba el reconocimiento de operadores relacionales de un solo caracter."""
        casos = [
            ("<", "LT"),
            (">", "GT"),
            ("=", "ASSIGN")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operadores_relacionales_regex(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    def test_operadores_compuestos(self):
        """Comprueba el reconocimiento de operadores relacionales de dos caracteres."""
        casos = [
            ("<=", "LE"),
            (">=", "GE"),
            ("==", "EQ"),
            ("!=", "NE")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operadores_relacionales_regex(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    def test_operadores_con_texto_extra(self):
        """Comprueba que se separe el operador de caracteres posteriores."""
        casos = [
            ("<=5", "<=", "LE"),
            ("==x", "==", "EQ"),
            ("> ", ">", "GT"),
            ("!=0", "!=", "NE")
        ]
        for entrada, lexema_esperado, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operadores_relacionales_regex(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, lexema_esperado)

    def test_entradas_invalidas(self):
        """Comprueba el rechazo de entradas inválidas como caracteres aislados '!' o texto vacío."""
        casos = ["", "a", "!", "1", "_"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operadores_relacionales_regex(entrada)
                self.assertFalse(es_valido)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()