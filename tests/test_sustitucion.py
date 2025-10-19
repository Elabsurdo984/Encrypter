import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ciphers.sustitucion import cifrado_sustitucion, generar_clave_sustitucion, cargar_clave_sustitucion

class TestSustitucion(unittest.TestCase):

    def setUp(self):
        # Create a dummy key file for testing
        generar_clave_sustitucion()

    def tearDown(self):
        # Remove the dummy key file
        os.remove('subst.key')

    def test_cifrado_sustitucion(self):
        texto_original = "Hola Mundo"
        clave = cargar_clave_sustitucion()
        texto_cifrado = cifrado_sustitucion(texto_original, clave, 'encrypt')
        self.assertNotEqual(texto_original, texto_cifrado)
        texto_descifrado = cifrado_sustitucion(texto_cifrado, clave, 'decrypt')
        self.assertEqual(texto_original, texto_descifrado)

if __name__ == '__main__':
    unittest.main()
