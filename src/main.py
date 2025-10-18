import argparse
import os

from ciphers.cesar import cifrado_cesar
from ciphers.sustitucion import (
    generar_clave_sustitucion,
    cargar_clave_sustitucion,
    cifrado_sustitucion,
)
from ciphers.transposicion import cifrar_transposicion, descifrar_transposicion


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
        output_path = os.path.splitext(args.filepath)[0] + ".ic"
    else: # decrypt
        if args.filepath.endswith(".ic"):
             output_path = args.filepath.replace(".ic", "")
        else:
             output_path = os.path.splitext(args.filepath)[0] + ".dec"

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(contenido_procesado)

    print(f"Archivo procesado con '{args.cipher}'. Resultado guardado en '{output_path}'")


if __name__ == "__main__":
    main()
