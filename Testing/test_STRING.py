import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import STRING as lexer  # type: ignore

class TestString(unittest.TestCase):

    def test_cadenas_validas(self):
        """Comprueba el reconocimiento de cadenas bien formadas."""
        casos = [
            ('""', '""'),
            ('"hola"', '"hola"'),
            ('"123 abC!"', '"123 abC!"')
        ]
        for entrada, lexema_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_cadena(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, "STRING")
                self.assertEqual(lexema, lexema_esperado)
                
    def test_cadena_con_texto_extra(self):
        """Comprueba que separa la cadena si hay algo después de la comilla final."""
        casos = [
            ('"hola" extra', '"hola"'),
            ('""+', '""')
        ]
        for entrada, lexema_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_cadena(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, "STRING")
                self.assertEqual(lexema, lexema_esperado)

    def test_cadenas_invalidas(self):
        """Comprueba el rechazo de cadenas no terminadas, con saltos de línea o sin comilla de inicio."""
        casos = ["", "hola", '"', '"hola', '"hola\n"']
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_cadena(entrada)
                self.assertFalse(es_valido)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()