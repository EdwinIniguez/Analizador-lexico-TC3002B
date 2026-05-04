import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import NUMBER as lexer  # type: ignore

class TestNumber(unittest.TestCase):

    # Primer test
    # Prueba que los numeros sin punto se reconozcan como ENTEROS
    def test_numeros_enteros(self):
        casos = ["0", "1", "42", "9999"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, subtipo, lexema, msg = lexer.reconocer_numero(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, "NUMBER")
                self.assertEqual(subtipo, "ENTERO")
                self.assertEqual(lexema, entrada)

    # Segundo test
    # Prueba que los numeros con punto se reconozcan como DECIMALES
    def test_numeros_decimales(self):
        casos = ["0.0", "3.14", "99.99"]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, subtipo, lexema, msg = lexer.reconocer_numero(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, "NUMBER")
                self.assertEqual(subtipo, "DECIMAL")
                self.assertEqual(lexema, entrada)

    # Tecer Test
    # Prueba que detenga la captura del numero si se topa con un caracter no numerico
    def test_numeros_con_texto_extra(self):
        casos = [
            ("42x", "42", "ENTERO"),
            ("3.14+", "3.14", "DECIMAL"),
            ("0.5.2", "0.5", "DECIMAL")  # En este caso, se detiene al segundo punto
        ]
        for entrada, lexema_esperado, subtipo_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, subtipo, lexema, msg = lexer.reconocer_numero(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, "NUMBER")
                self.assertEqual(subtipo, subtipo_esperado)
                self.assertEqual(lexema, lexema_esperado)

    # Cuarto test
    # Prueba que tire error al iniciar con caracteres no numericos o dejar un punto colgando
    def test_errores_en_numeros(self):
        casos = ["", "a", ".", "3."]
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, subtipo, lexema, msg = lexer.reconocer_numero(entrada)
                self.assertFalse(es_valido)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()