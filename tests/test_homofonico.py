import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ciphers.homofonico import encrypt, decrypt, generar_clave_homofonica, cargar_clave_homofonica

class TestHomofonico(unittest.TestCase):

    def setUp(self):
        # Create a dummy key file for testing
        generar_clave_homofonica()

    def tearDown(self):
        # Remove the dummy key file
        os.remove('homofonico.key')

    def test_cifrado_homofonico(self):
        texto_original = "Hola Mundo"
        clave = cargar_clave_homofonica()
        texto_cifrado = encrypt(texto_original, clave)
        self.assertNotEqual(texto_original, texto_cifrado)
        texto_descifrado = decrypt(texto_cifrado, clave)
        self.assertEqual(texto_original.upper().replace(" ", ""), texto_descifrado)

if __name__ == '__main__':
    unittest.main()
