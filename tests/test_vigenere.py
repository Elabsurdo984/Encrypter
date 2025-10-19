import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ciphers.vigenere import cifrado_vigenere

class TestVigenere(unittest.TestCase):

    def test_cifrado_vigenere(self):
        texto_original = "Hola Mundo"
        clave = "LEMON"
        texto_cifrado = cifrado_vigenere(texto_original, clave, 'encrypt')
        self.assertNotEqual(texto_original, texto_cifrado)
        texto_descifrado = cifrado_vigenere(texto_cifrado, clave, 'decrypt')
        self.assertEqual(texto_original, texto_descifrado)

if __name__ == '__main__':
    unittest.main()
