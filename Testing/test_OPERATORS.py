import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import OPERATORS as lexer  # type: ignore

class TestOperators(unittest.TestCase):

    def test_operadores_simples(self):
        """Comprueba el reconocimiento de operadores de un solo caracter."""
        casos = [
            ("+", "PLUS"),
            ("-", "MINUS"),
            ("*", "TIMES"),
            ("/", "DIVIDE"),
            ("%", "MOD")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operador_aritmetico(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    def test_operadores_compuestos(self):
        """Comprueba el reconocimiento de operadores de dos caracteres."""
        casos = [
            ("**", "POWER"),
            ("//", "FLOORDIV")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operador_aritmetico(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    def test_operadores_con_texto(self):
        """Comprueba que separe adecuadamente el operador del resto de la cadena."""
        casos = [
            ("+5", "+", "PLUS"),
            ("**2", "**", "POWER"),
            ("//x", "//", "FLOORDIV"),
            ("* ", "*", "TIMES")
        ]
        for entrada, lexema_esperado, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operador_aritmetico(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, lexema_esperado)

    def test_entradas_invalidas(self):
        """Comprueba que detenga o reporte error con entradas inválidas."""
        casos = ["", "a", "1", "_"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operador_aritmetico(entrada)
                self.assertFalse(es_valido)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()