# --- Lógica de Cifrado César ---

def cifrado_cesar(texto, desplazamiento, modo):
    """Cifra o descifra el texto usando el Cifrado César."""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''
    if modo == 'decrypt':
        desplazamiento = -desplazamiento
    for caracter in texto:
        if caracter.lower() in alfabeto:
            idx = alfabeto.find(caracter.lower())
            nuevo_idx = (idx + desplazamiento) % len(alfabeto)
            if caracter.isupper():
                resultado += alfabeto[nuevo_idx].upper()
            else:
                resultado += alfabeto[nuevo_idx]
        else:
            resultado += caracter
    return resultado
