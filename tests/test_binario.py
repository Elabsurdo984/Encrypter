import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ciphers.binario import encrypt, decrypt

class TestBinario(unittest.TestCase):

    def test_cifrado_binario(self):
        texto_original = "Hola Mundo"
        texto_cifrado = encrypt(texto_original)
        self.assertNotEqual(texto_original, texto_cifrado)
        texto_descifrado = decrypt(texto_cifrado)
        self.assertEqual(texto_original, texto_descifrado)

if __name__ == '__main__':
    unittest.main()
