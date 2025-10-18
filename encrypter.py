import argparse
import os
import random
import math

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


# --- Lógica del CLI ---

def main():
    parser = argparse.ArgumentParser(description="CLI para encriptar y desencriptar archivos con varios cifrados.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Comando 'genkey' ---
    genkey_parser = subparsers.add_parser("genkey", help="Genera una nueva clave de encriptación.")
    genkey_parser.add_argument("ciphertype", type=str, choices=['substitution'], help="Tipo de clave a generar (solo 'substitution' disponible).")

    # --- Comando 'encrypt' ---
    encrypt_parser = subparsers.add_parser("encrypt", help="Encripta un archivo.")
    encrypt_parser.add_argument("filepath", type=str, help="Ruta del archivo a encriptar.")
    encrypt_parser.add_argument("-c", "--cipher", type=str, required=True, choices=['caesar', 'substitution', 'transposition'], help="El cifrado a utilizar.")
    encrypt_parser.add_argument("-s", "--shift", type=int, help="El desplazamiento para César o la clave para Transposición.")

    # --- Comando 'decrypt' ---
    decrypt_parser = subparsers.add_parser("decrypt", help="Desencripta un archivo.")
    decrypt_parser.add_argument("filepath", type=str, help="Ruta del archivo a desencriptar.")
    decrypt_parser.add_argument("-c", "--cipher", type=str, required=True, choices=['caesar', 'substitution', 'transposition'], help="El cifrado a utilizar.")
    decrypt_parser.add_argument("-s", "--shift", type=int, help="El desplazamiento para César o la clave para Transposición.")

    args = parser.parse_args()

    # --- Lógica de ejecución ---
    
    if args.command == "genkey":
        if args.ciphertype == 'substitution':
            generar_clave_sustitucion()
        return

    # Leer archivo de entrada
    try:
        with open(args.filepath, 'r', encoding='utf-8') as file:
            contenido = file.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{args.filepath}' no fue encontrado.")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Procesar según el cifrado
    contenido_procesado = ""
    if args.cipher == 'caesar':
        if args.shift is None:
            print("Error: El cifrado César requiere el argumento --shift.")
            return
        contenido_procesado = cifrado_cesar(contenido, args.shift, args.command)
    
    elif args.cipher == 'substitution':
        try:
            clave = cargar_clave_sustitucion()
            contenido_procesado = cifrado_sustitucion(contenido, clave, args.command)
        except FileNotFoundError:
            print("Error: No se encuentra 'subst.key'. Genera una clave con 'encrypter genkey substitution'.")
            return

    elif args.cipher == 'transposition':
        if args.shift is None:
            print("Error: El cifrado por transposición requiere el argumento --shift (clave).")
            return
        if args.command == 'encrypt':
            contenido_procesado = cifrar_transposicion(contenido, args.shift)
        else: # decrypt
            contenido_procesado = descifrar_transposicion(contenido, args.shift)

    # Escribir archivo de salida
    if args.command == 'encrypt':
        output_path = args.filepath + f".{args.cipher}"
    else: # decrypt
        if args.filepath.endswith(f".{args.cipher}"):
             output_path = args.filepath.replace(f".{args.cipher}", "")
        else:
             output_path = os.path.splitext(args.filepath)[0] + ".dec"

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(contenido_procesado)

    print(f"Archivo procesado con '{args.cipher}'. Resultado guardado en '{output_path}'")


if __name__ == "__main__":
    main()
