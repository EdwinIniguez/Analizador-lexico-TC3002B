import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import FOR_IN_IS_AND_OR_NOT as lexer  # type: ignore

class TestAnalizadorLexicoRegex(unittest.TestCase):
    # Primer Test
    # Prueba que los keywords exactos sean reconocidos con el token correcto
    def test_reconocimiento_keywords(self):
        casos = [
            ("for", "FOR"),
            ("in", "IN"),
            ("is", "IS"),
            ("and", "AND"),
            ("or", "OR"),
            ("not", "NOT")
        ]

        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertTrue(es_kw)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    # Segundo Test
    # Prueba que si una palabra comienza con el keyword pero continua, sea un NAME
    def test_prefijos_de_keywords_son_names(self):
        casos = ["format", "inside", "issue", "android", "oracle", "nothing"]
        
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    # Tercer test
    # Prueba identificadores validos o caracteres que no deben ser clasificados como keywords
    def test_identificadores_regulares(self):
        casos = ["variable", "x", "_contador", "v123"]

        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
    
    # Cuarto test
    # Prueba que las cadenas vacias manejen el error correctamente
    def test_cadenas_vacias(self):
        es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex("")
        self.assertFalse(es_kw)
        self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()