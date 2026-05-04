import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import SPECIAL_SYMBOLS as lexer  # type: ignore

class TestSpecialSymbols(unittest.TestCase):

    # Primer test 
    # Prueba que los simbolos especiales de un solo caracter sean reconocidos
    def test_simbolos_simples(self):
        casos = [
            (",", "COMMA"),
            (":", "COLON"),
            (".", "DOT"),
            ("@", "AT"),
            ("~", "TILDE"),
            ("&", "AMPERSAND"),
            ("`", "PIPE"),
            ("^", "CARET")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_simbolo, tipo, lexema, msg = lexer.reconocer_simbolo_especial(entrada)
                self.assertTrue(es_simbolo)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    # Segundo test
    # Prueba que los simbolos especiales de dos caracteres sean reconocidos
    def test_simbolos_compuestos(self):
        casos = [
            ("->", "ARROW"),
            ("<<", "LSHIFT"),
            (">>", "RSHIFT")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_simbolo, tipo, lexema, msg = lexer.reconocer_simbolo_especial(entrada)
                self.assertTrue(es_simbolo)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    # Tercer test
    # Prueba que se separe el simbolo de otros caracteres
    def test_simbolos_con_texto_extra(self):
        casos = [
            ("->x", "->", "ARROW"),
            ("<<5", "<<", "LSHIFT"),
            (", ", ",", "COMMA"),
            (":@", ":", "COLON")
        ]
        for entrada, lexema_esperado, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_simbolo, tipo, lexema, msg = lexer.reconocer_simbolo_especial(entrada)
                self.assertTrue(es_simbolo)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, lexema_esperado)

    # Cuarto test
    # Prueba que detenga o reporte error con entradas invalidas
    def test_entradas_invalidas(self):
        casos = ["", "a", "-", "<", ">", "1"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_simbolo, tipo, lexema, msg = lexer.reconocer_simbolo_especial(entrada)
                self.assertFalse(es_simbolo)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()