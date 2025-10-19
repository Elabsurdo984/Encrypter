def encrypt(text):
    """
    Encrypts a text using binary representation of characters.
    """
    return ' '.join(format(ord(char), '08b') for char in text)

def decrypt(text):
    """
    Decrypts a text from binary representation to characters.
    """
    return ''.join(chr(int(binary, 2)) for binary in text.split())
