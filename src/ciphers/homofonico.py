import random
import json

# Frecuencias aproximadas de las letras en español
FRECUENCIAS = {
    'E': 9, 'A': 9, 'O': 7, 'S': 7, 'N': 6, 'R': 7, 'I': 6, 'L': 6, 'D': 6,
    'U': 5, 'T': 5, 'C': 5, 'M': 3, 'P': 3, 'B': 2, 'G': 2, 'V': 2, 'Y': 1,
    'Q': 1, 'H': 1, 'F': 1, 'Z': 1, 'J': 1, 'Ñ': 1, 'X': 1, 'K': 1, 'W': 1
}

def generar_mapa_homofonico():
    """
    Genera un mapa homofónico basado en las frecuencias de las letras en español.
    """
    mapa = {}
    numeros = list(range(100))
    random.shuffle(numeros)
    
    for letra, freq in FRECUENCIAS.items():
        mapa[letra] = [str(numeros.pop()) for _ in range(freq)]
        mapa[letra.lower()] = mapa[letra]

    return mapa

def encrypt(text, mapa):
    """
    Cifra el texto usando un mapa homofónico.
    """
    encrypted_text = []
    for char in text:
        if char in mapa:
            encrypted_text.append(random.choice(mapa[char]))
        else:
            encrypted_text.append(char)
    return ' '.join(encrypted_text)

def decrypt(text, mapa):
    """
    Descifra el texto usando un mapa homofónico.
    """
    decrypted_text = ""
    mapa_inverso = {num: letra for letra, numeros in mapa.items() for num in numeros if letra.isupper()}
    
    for num in text.split():
        if num in mapa_inverso:
            decrypted_text += mapa_inverso[num]
        else:
            decrypted_text += num
    return decrypted_text

def generar_clave_homofonica():
    """Genera una clave homofónica y la guarda en un archivo."""
    mapa = generar_mapa_homofonico()
    with open("homofonico.key", "w", encoding='utf-8') as key_file:
        json.dump(mapa, key_file)
    print("¡Clave homofónica generada y guardada en 'homofonico.key'!")

def cargar_clave_homofonica():
    """Carga la clave homofónica desde el archivo."""
    with open("homofonico.key", "r", encoding='utf-8') as key_file:
        return json.load(key_file)
