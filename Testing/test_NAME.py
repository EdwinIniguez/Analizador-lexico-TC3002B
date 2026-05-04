import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import NAME as lexer  # type: ignore

class TestName(unittest.TestCase):

    # Primer test
    # Prueba que los identificadores validos se reconozcan completamente
    def test_nombres_validos(self):
        casos = ["variable", "x", "_contador", "v123", "MiClase_12"]

        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_identificador(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, entrada)

    # Segundo test
    # Prueba que se detenga el reconocimiento al encontrar un caracter no valido
    def test_nombres_con_caracteres_invalidos(self):
        casos = [
            ("var!iable", "var"),
            ("nombre@correo", "nombre"),
            ("ident#ificador", "ident")
        ]

        for entrada, lexema_esperado in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_identificador(entrada)
                self.assertTrue(es_valido)
                self.assertEqual(tipo, "NAME")
                self.assertEqual(lexema, lexema_esperado)
    
    # Tercer Test
    # Prueba que tire error si la cadena empieza con numeros u otros caracteres
    def test_inicios_invalidos(self):
        casos = ["1var", "@var", "!nombre", ""]

        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_valido, tipo, lexema, msg = lexer.reconocer_identificador(entrada)
                self.assertFalse(es_valido)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()