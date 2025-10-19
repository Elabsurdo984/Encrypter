import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ciphers.cesar import cifrado_cesar

class TestCesar(unittest.TestCase):

    def test_cifrado_cesar(self):
        texto_original = "Hola Mundo"
        shift = 3
        texto_cifrado = cifrado_cesar(texto_original, shift, 'encrypt')
        self.assertNotEqual(texto_original, texto_cifrado)
        texto_descifrado = cifrado_cesar(texto_cifrado, shift, 'decrypt')
        self.assertEqual(texto_original, texto_descifrado)

if __name__ == '__main__':
    unittest.main()
