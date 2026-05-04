import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import TRUE_FALSE_NONE_PASS_BREAK_CONTINUE as lexer  # type: ignore

class TestTrueFalseNonePassBreakContinue(unittest.TestCase):
    
    # Primer Test
    # Prueba que los keywords exactos sean reconocidos como tokens validos
    def test_reconocimiento_keywords(self):
        casos = [
            ("VERDADERO", "VERDADERO"),
            ("FALSO", "FALSO"),
            ("None", "NONE"),
            ("pass", "PASS"),
            ("break", "BREAK"),
            ("continue", "CONTINUE")
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
        casos = ["VERDADEROS", "FALSO1", "None_", "password", "breakdown", "continues"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    # Tercer test
    # Prueba identificadores validos o caracteres que no deben ser clasificados como DEF/RETURN
    def test_identificadores_regulares_y_errores(self):
        casos = ["variable", "x", "_contador", "", "!"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                # Unos serán NAME y otros ERROR
                self.assertIn(tipo, ["NAME", "ERROR"])
                
if __name__ == '__main__':
    unittest.main()