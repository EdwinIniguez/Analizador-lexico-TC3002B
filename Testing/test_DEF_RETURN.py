import unittest
import sys
import os

# Agregar ruta de la carpeta "Source" al path del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import DEF_RETURN as lexer  # type: ignore

class TestDefReturnRegex(unittest.TestCase):

    # Primer Test
    # Prueba que los keywords exactos sean reconocidos como tokens validos
    def test_reconocimiento_keywords(self):
        casos = [
            ("def", "DEF"),
            ("return", "RETURN")
        ]
        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertTrue(es_kw)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    # Segundo Test
    # Prueba que palabras que comienzan con keywords, pero continuan, sean NAME
    def test_prefijos_de_keywords_son_names(self):
        casos = ["define", "default", "returning", "returns", "def_val"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    # Tercer test
    # Prueba identificadores validos o caracteres que no deben ser clasificados como DEF/RETURN
    def test_identificadores_o_errores(self):
        casos = ["variable", "d", "r", "x_1", "funcion"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertIn(tipo, ["NAME", "ERROR"])
                
if __name__ == '__main__':
    unittest.main()