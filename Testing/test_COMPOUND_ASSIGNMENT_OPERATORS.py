import unittest
import sys
import os

# Agregar ruta de la carpeta "Source" al path del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Source')))

import COMPOUND_ASSIGNMENT_OPERATORS as lexer  # type: ignore

class TestOperadoresAsignacion(unittest.TestCase):
    
    # Primer test
    # prueba que los operadores exactos sean reconocidos correctamente
    def test_reconocimiento_operadores_exactos(self):
        casos = [
            ("+=", "PLUSEQ"),
            ("-=", "MINUSEQ"),
            ("*=", "TIMESEQ"),
            ("/=", "DIVEQ")
        ]

        for entrada, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_op, tipo, lexema, msg = lexer.reconocer_operadores_asignacion_compuesta(entrada)
                self.assertTrue(es_op)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, entrada)

    # Segundo test
    # Prueba que los operadores se separen del texto extra (ej: +=5)
    def test_operadores_con_texto_extra(self):
        
        casos = [
            ("+=5", "+=", "PLUSEQ"),
            ("-=x", "-=", "MINUSEQ"),
            ("*= ", "*=", "TIMESEQ"),
            ("/=2", "/=", "DIVEQ")
        ]
        
        for entrada, lexema_esperado, token_esperado in casos:
            with self.subTest(entrada=entrada):
                es_op, tipo, lexema, msg = lexer.reconocer_operadores_asignacion_compuesta(entrada)
                self.assertTrue(es_op)
                self.assertEqual(tipo, token_esperado)
                self.assertEqual(lexema, lexema_esperado)

    # Tercer test
    # Prueba entradas que no son operadores de asignacion compuesta    
    def test_entradas_invalidas_incompletas(self):
        casos = ["+", "-", "*", "/", "++", "--", "==5", ""]
        
        for entrada in casos:
            with self.subTest(entrada=entrada):
                es_op, tipo, lexema, msg = lexer.reconocer_operadores_asignacion_compuesta(entrada)
                self.assertFalse(es_op)
                self.assertEqual(tipo, "ERROR")

if __name__ == '__main__':
    unittest.main()