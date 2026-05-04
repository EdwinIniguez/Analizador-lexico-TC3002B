import unittest
import sys
import os

# Agregamos la ruta de la carpeta "Source" al path del sistema para poder hacer el import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

# Importamos el analizador léxico
import FOR_IN_IS_AND_OR_NOT as lexer  # type: ignore

class TestAnalizadorLexicoRegex(unittest.TestCase):

    def test_reconocimiento_keywords(self):
        """Prueba que los keywords exactos sean reconocidos con el token correcto."""
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

    def test_prefijos_de_keywords_son_names(self):
        """Prueba que si una palabra comienza con el keyword pero continúa, sea un NAME."""
        casos = ["format", "inside", "issue", "android", "oracle", "nothing"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    def test_identificadores_regulares(self):
        """Prueba identificadores válidos que no coinciden con ningún keyword en su inicio."""
        casos = ["variable", "x", "_contador", "v123"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex(entrada)
                self.assertFalse(es_kw)
                self.assertEqual(tipo, "NAME")
                
    def test_cadenas_vacias(self):
        """Prueba que las cadenas vacías manejen el error correctamente."""
        es_kw, tipo, lexema, msg = lexer.reconocer_keyword_regex("")
        self.assertFalse(es_kw)
        self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()