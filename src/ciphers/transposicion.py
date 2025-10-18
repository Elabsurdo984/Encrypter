import math

# --- Lógica de Cifrado por Transposición ---

def cifrar_transposicion(texto, clave):
    """Cifra el texto usando el Cifrado por Transposición."""
    columnas = [''] * clave
    for col in range(clave):
        puntero = col
        while puntero < len(texto):
            columnas[col] += texto[puntero]
            puntero += clave
    return ''.join(columnas)

def descifrar_transposicion(texto_cifrado, clave):
    """Descifra el texto usando el Cifrado por Transposición."""
    num_columnas = int(math.ceil(len(texto_cifrado) / float(clave)))
    num_filas = clave
    num_cajas_sombreadas = (num_columnas * num_filas) - len(texto_cifrado)
    
    texto_plano = [''] * num_columnas
    col = 0
    fila = 0
    
    for simbolo in texto_cifrado:
        texto_plano[col] += simbolo
        col += 1
        if (col == num_columnas) or (col == num_columnas - 1 and fila >= num_filas - num_cajas_sombreadas):
            col = 0
            fila += 1
            
    return ''.join(texto_plano)
