import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import WHILE as lexer  # type: ignore

class TestWhile(unittest.TestCase):

    # Primer Test
    # Comprueba que 'while' sea reconocido perfectamente
    def test_reconocimiento_exacto(self):
        es_kw, tipo, lexema, msg = lexer.reconocer_while("while")
        self.assertTrue(es_kw)
        self.assertEqual(tipo, "WHILE")
        self.assertEqual(lexema, "while")

    # Segundo test
    # Comprueba que identificadores que inician con 'while' sean marcados como NAME
    def test_prefijos_identificadores(self):
        casos = ["while1", "while_loop", "whiler"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_while(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    # Tercer Test
    # Comprueba identificadores que empiezan con w pero no son while
    def test_identificadores_incompletos(self):
        casos = ["w", "wh", "whi", "whil", "wolf"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_while(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    # Cuarto test
    # Comprueba entradas invalidas
    def test_entradas_invalidas(self):
        casos = ["", "1", "x", "!"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_while(entrada)
                self.assertFalse(es_kw)

if __name__ == '__main__':
    unittest.main()