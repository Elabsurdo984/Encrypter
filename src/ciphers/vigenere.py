def cifrado_vigenere(texto, clave, modo):
    """Cifra o descifra el texto usando el Cifrado Vigenère."""
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''
    clave_idx = 0
    clave = clave.lower()

    for caracter in texto:
        if caracter.lower() in alfabeto:
            if modo == 'decrypt':
                desplazamiento = -alfabeto.find(clave[clave_idx])
            else:
                desplazamiento = alfabeto.find(clave[clave_idx])

            idx = alfabeto.find(caracter.lower())
            nuevo_idx = (idx + desplazamiento) % len(alfabeto)

            if caracter.isupper():
                resultado += alfabeto[nuevo_idx].upper()
            else:
                resultado += alfabeto[nuevo_idx]

            clave_idx = (clave_idx + 1) % len(clave)
        else:
            resultado += caracter

    return resultado
