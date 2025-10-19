import unittest
import os
import subprocess

class TestMain(unittest.TestCase):

    def setUp(self):
        self.test_file = 'tests/test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('Hola Mundo')

    def tearDown(self):
        files_to_remove = [
            self.test_file,
            'tests/test_file.ic',
            'tests/test_file',
            'subst.key',
            'homofonico.key'
        ]
        for f in files_to_remove:
            if os.path.exists(f):
                os.remove(f)

    def test_cli_homofonico(self):
        # Generate key
        command = ['python', 'src/main.py', 'genkey', 'homophonic']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('homofonico.key'))

        # Encrypt
        command = ['python', 'src/main.py', 'encrypt', self.test_file, '-c', 'homophonic']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file.ic'))

        # Decrypt
        command = ['python', 'src/main.py', 'decrypt', 'tests/test_file.ic', '-c', 'homophonic']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file'))

        with open('tests/test_file', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'HOLAMUNDO')

    def run_command(self, command):
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command: {' '.join(command)}")
            print(f"stdout: {result.stdout}")
            print(f"stderr: {result.stderr}")
        return result

    def test_cli_cesar(self):
        # Encrypt
        command = ['python', 'src/main.py', 'encrypt', self.test_file, '-c', 'caesar', '-s', '3']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file.ic'))

        # Decrypt
        command = ['python', 'src/main.py', 'decrypt', 'tests/test_file.ic', '-c', 'caesar', '-s', '3']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file'))

        with open('tests/test_file', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Hola Mundo')

    def test_cli_sustitucion(self):
        # Generate key
        command = ['python', 'src/main.py', 'genkey', 'substitution']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('subst.key'))

        # Encrypt
        command = ['python', 'src/main.py', 'encrypt', self.test_file, '-c', 'substitution']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file.ic'))

        # Decrypt
        command = ['python', 'src/main.py', 'decrypt', 'tests/test_file.ic', '-c', 'substitution']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file'))

        with open('tests/test_file', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Hola Mundo')

    def test_cli_transposicion(self):
        # Encrypt
        command = ['python', 'src/main.py', 'encrypt', self.test_file, '-c', 'transposition', '-s', '8']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file.ic'))

        # Decrypt
        command = ['python', 'src/main.py', 'decrypt', 'tests/test_file.ic', '-c', 'transposition', '-s', '8']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file'))

        with open('tests/test_file', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Hola Mundo')

    def test_cli_vigenere(self):
        # Encrypt
        command = ['python', 'src/main.py', 'encrypt', self.test_file, '-c', 'vigenere', '-k', 'LEMON']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file.ic'))

        # Decrypt
        command = ['python', 'src/main.py', 'decrypt', 'tests/test_file.ic', '-c', 'vigenere', '-k', 'LEMON']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file'))

        with open('tests/test_file', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Hola Mundo')

    def test_cli_binario(self):
        # Encrypt
        command = ['python', 'src/main.py', 'encrypt', self.test_file, '-c', 'binario']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file.ic'))

        # Decrypt
        command = ['python', 'src/main.py', 'decrypt', 'tests/test_file.ic', '-c', 'binario']
        result = self.run_command(command)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists('tests/test_file'))

        with open('tests/test_file', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Hola Mundo')

if __name__ == '__main__':
    unittest.main()