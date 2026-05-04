import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import STRING as lexer  # type: ignore

class TestString(unittest.TestCase):

    # Primer Test
    # Comprueba el reconocimiento de cadenas bien formadas
    def test_cadenas_validas(self):
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
                
    # Segundo Test
    # Comprueba que separa la cadena si hay algo despues de la comilla final
    def test_cadena_con_texto_extra(self):
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

    # Cuarto test
    # Comprueba el rechazo de cadenas no terminadas, con saltos de linea o sin comilla de inicio
    def test_cadenas_invalidas(self):
        casos = ["", "hola", '"', '"hola', '"hola\n"']
        
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_cadena(entrada)
                self.assertFalse(es_valido)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()