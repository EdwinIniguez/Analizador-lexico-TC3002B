import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import DELIMITERS as lexer  # type: ignore

class TestDelimiters(unittest.TestCase):

    # Primer test
    # Comprueba que todos los delimitadores se detecten de forma correcta
    def test_reconocimiento_exacto(self):
        casos = [
            ("(", "LPAREN"),
            (")", "RPAREN"),
            ("[", "LBRACKET"),
            ("]", "RBRACKET"),
            ("{", "LBRACE"),
            ("}", "RBRACE")
        ]
        
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_delimitador, tipo, lexema, msg = lexer.reconocer_delimitador(entrada)
                self.assertTrue(es_delimitador)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    # Segundo test
    # Comprueba que el lexema extraiga solo el delimitador si va pegado a otras cosas
    def test_delimitadores_con_texto(self):
        casos = [
            ("(x", "(", "LPAREN"),
            ("] ", "]", "RBRACKET"),
            ("{def", "{", "LBRACE")
        ]

        for entrada, lexema_esperado, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_delimitador, tipo, lexema, msg = lexer.reconocer_delimitador(entrada)
                self.assertTrue(es_delimitador)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, lexema_esperado)

    # Tercer Test
    # Comprueba entradas invalidas
    def test_entradas_invalidas(self):
        casos = ["", "a", "+", "123"]
        
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_delimitador, tipo, lexema, msg = lexer.reconocer_delimitador(entrada)
                self.assertFalse(es_delimitador)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()