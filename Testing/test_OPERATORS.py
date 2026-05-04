import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import OPERATORS as lexer  # type: ignore

class TestOperators(unittest.TestCase):

    # Primer test
    #  Comprueba el reconocimiento de operadores de un solo caracter
    def test_operadores_simples(self):
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

    # Segundo test
    # Comprueba el reconocimiento de operadores de dos caracteres
    def test_operadores_compuestos(self):
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

    # Tercer test
    # Comprueba que separe adecuadamente el operador del resto de la cadena
    def test_operadores_con_texto(self):
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

    # Cuarto test
    # Comprueba que detenga o reporte error con entradas invalidas
    def test_entradas_invalidas(self):
        casos = ["", "a", "1", "_"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_operador_aritmetico(entrada)
                self.assertFalse(es_valido)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()