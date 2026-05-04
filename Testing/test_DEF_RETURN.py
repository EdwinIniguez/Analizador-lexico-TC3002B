import unittest
import sys
import os

# Agregamos la ruta de la carpeta "Source" al path del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import DEF_RETURN as lexer  # type: ignore

class TestDefReturnRegex(unittest.TestCase):

    def test_reconocimiento_keywords(self):
        """Prueba que los keywords exactos sean reconocidos como tokens válidos."""
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

    def test_prefijos_de_keywords_son_names(self):
        """Prueba que palabras que comienzan con keywords, pero continúan, sean NAME."""
        casos = ["define", "default", "returning", "returns", "def_val"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    def test_identificadores_o_errores(self):
        """Prueba identificadores válidos o caracteres que no deben ser clasificados como DEF/RETURN."""
        casos = ["variable", "d", "r", "x_1", "funcion"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                # Pueden ser clasificados como NAME (identificador) o ERROR dependiendo de si empieza con letra.
                # Sabemos que al menos no deben ser reconocidos como keyword ni dar un tipo DEF o RETURN.
                self.assertIn(tipo, ["NAME", "ERROR"])
                
if __name__ == '__main__':
    unittest.main()