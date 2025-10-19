import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ciphers.transposicion import cifrar_transposicion, descifrar_transposicion

class TestTransposicion(unittest.TestCase):

    def test_cifrado_transposicion(self):
        texto_original = "Hola Mundo"
        clave = 8
        texto_cifrado = cifrar_transposicion(texto_original, clave)
        self.assertNotEqual(texto_original, texto_cifrado)
        texto_descifrado = descifrar_transposicion(texto_cifrado, clave)
        self.assertEqual(texto_original, texto_descifrado)

if __name__ == '__main__':
    unittest.main()
