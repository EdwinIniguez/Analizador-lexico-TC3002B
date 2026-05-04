import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import WHILE as lexer  # type: ignore

class TestWhile(unittest.TestCase):

    def test_reconocimiento_exacto(self):
        """Comprueba que 'while' sea reconocido perfectamente."""
        es_kw, tipo, lexema, msg = lexer.reconocer_while("while")
        self.assertTrue(es_kw)
        self.assertEqual(tipo, "WHILE")
        self.assertEqual(lexema, "while")

    def test_prefijos_identificadores(self):
        """Comprueba que identificadores que inician con 'while' sean marcados como NAME."""
        casos = ["while1", "while_loop", "whiler"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_while(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)
                
    def test_identificadores_incompletos(self):
        """Comprueba identificadores que empiezan con w pero no son while."""
        casos = ["w", "wh", "whi", "whil", "wolf"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_while(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    def test_entradas_invalidas(self):
        """Comprueba que arroje un error si le pasamos palabras que no empiezan con letras o _."""
        casos = ["", "1", "x", "!"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_while(entrada)
                self.assertFalse(es_kw)

if __name__ == '__main__':
    unittest.main()