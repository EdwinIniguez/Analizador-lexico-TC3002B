import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import SPECIAL_SYMBOLS as lexer  # type: ignore

class TestSpecialSymbols(unittest.TestCase):

    def test_simbolos_simples(self):
        """Prueba que los símbolos especiales de un solo caracter sean reconocidos."""
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

    def test_simbolos_compuestos(self):
        """Prueba que los símbolos especiales de dos caracteres sean reconocidos."""
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

    def test_simbolos_con_texto_extra(self):
        """Prueba que se separe el símbolo de otros caracteres."""
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

    def test_entradas_invalidas(self):
        """Prueba entradas que no corresponden a un símbolo válido o están incompletas."""
        casos = ["", "a", "-", "<", ">", "1"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_simbolo, tipo, lexema, msg = lexer.reconocer_simbolo_especial(entrada)
                self.assertFalse(es_simbolo)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()