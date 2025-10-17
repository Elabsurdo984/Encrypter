import argparse
import os

# --- Lógica del Cifrado César ---

def cifrado_cesar(texto, desplazamiento, modo):
    """
    Cifra o descifra el texto usando el Cifrado César.
    modo: 'encrypt' o 'decrypt'
    """
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    if modo == 'decrypt':
        desplazamiento = -desplazamiento

    for caracter in texto:
        if caracter.lower() in alfabeto:
            # Encontrar la posición del caracter en el alfabeto
            idx = alfabeto.find(caracter.lower())
            # Calcular la nueva posición con el desplazamiento
            nuevo_idx = (idx + desplazamiento) % len(alfabeto)
            
            # Añadir el nuevo caracter al resultado, conservando mayúsculas/minúsculas
            if caracter.isupper():
                resultado += alfabeto[nuevo_idx].upper()
            else:
                resultado += alfabeto[nuevo_idx]
        else:
            # Si el caracter no está en el alfabeto, se mantiene igual
            resultado += caracter
            
    return resultado

# --- Lógica de archivos ---

def procesar_archivo(filepath, desplazamiento, modo):
    """Lee un archivo, lo cifra/descifra y guarda el resultado."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            contenido = file.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{filepath}' no fue encontrado.")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    contenido_procesado = cifrado_cesar(contenido, desplazamiento, modo)

    # Definir el nombre del archivo de salida
    if modo == 'encrypt':
        output_path = filepath + ".cesar"
    else: # decrypt
        if filepath.endswith(".cesar"):
             output_path = filepath.replace(".cesar", "")
        else:
             # Si el archivo no termina en .cesar, añade .dec para evitar sobreescribir
             output_path = os.path.splitext(filepath)[0] + ".dec"

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(contenido_procesado)
    
    if modo == 'encrypt':
        print(f"Archivo encriptado y guardado como '{output_path}'")
    else:
        print(f"Archivo desencriptado y guardado como '{output_path}'")


# --- Lógica del CLI ---

def main():
    parser = argparse.ArgumentParser(description="CLI para encriptar y desencriptar archivos con Cifrado César.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Comandos disponibles")

    # Comando para encriptar
    encrypt_parser = subparsers.add_parser("encrypt", help="Encripta un archivo usando Cifrado César.")
    encrypt_parser.add_argument("filepath", type=str, help="Ruta del archivo a encriptar.")
    encrypt_parser.add_argument("-s", "--shift", type=int, required=True, help="El número de posiciones a desplazar.")

    # Comando para desencriptar
    decrypt_parser = subparsers.add_parser("decrypt", help="Desencripta un archivo usando Cifrado César.")
    decrypt_parser.add_argument("filepath", type=str, help="Ruta del archivo a desencriptar.")
    decrypt_parser.add_argument("-s", "--shift", type=int, required=True, help="El número de posiciones a desplazar (la misma clave que al encriptar).")

    args = parser.parse_args()

    if args.command == "encrypt":
        procesar_archivo(args.filepath, args.shift, 'encrypt')
    elif args.command == "decrypt":
        procesar_archivo(args.filepath, args.shift, 'decrypt')

if __name__ == "__main__":
    main()
