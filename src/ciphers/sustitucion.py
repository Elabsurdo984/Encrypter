import random

# --- Lógica de Cifrado por Sustitución ---

def generar_clave_sustitucion():
    """Genera una clave de sustitución (alfabeto desordenado) y la guarda."""
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alfabeto)
    clave = "".join(alfabeto)
    with open("subst.key", "w", encoding='utf-8') as key_file:
        key_file.write(clave)
    print("¡Clave de sustitución generada y guardada en 'subst.key'!")

def cargar_clave_sustitucion():
    """Carga la clave de sustitución desde el archivo."""
    with open("subst.key", "r", encoding='utf-8') as key_file:
        return key_file.read()

def cifrado_sustitucion(texto, clave, modo):
    """Cifra o descifra el texto usando una clave de sustitución."""
    alfabeto_plano = 'abcdefghijklmnopqrstuvwxyz'
    
    # str.maketrans es una forma muy eficiente de crear tablas de traducción
    if modo == 'encrypt':
        mapa = str.maketrans(alfabeto_plano + alfabeto_plano.upper(), clave + clave.upper())
    else: # decrypt
        mapa = str.maketrans(clave + clave.upper(), alfabeto_plano + alfabeto_plano.upper())
        
    return texto.translate(mapa)
