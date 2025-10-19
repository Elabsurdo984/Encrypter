# Icryptian

Una sencilla herramienta de línea de comandos (CLI) para encriptar y desencriptar archivos utilizando cifrados clásicos. Creado en Python.

## Características

- **Cifrado César**: Encripta y desencripta archivos de texto.
- **Cifrado por Sustitución**: Utiliza un alfabeto desordenado como clave.
- **Cifrado por Transposición**: Cambia la posición de los caracteres usando una clave numérica.
- **Cifrado Vigenère**: Utiliza una clave de texto para mayor seguridad.
- **Cifrado Binario**: Convierte el texto a su representación binaria.
- **Cifrado Homofónico**: Oculta las frecuencias de las letras asignando múltiples sustitutos.
- **Empaquetado**: Se distribuye como un único ejecutable de Windows (`.exe`).

## Instalación

Para instalar `Icryptian` en tu sistema, sigue estos pasos:

1.  Ve a la sección de [Releases](https://github.com/Elabsurdo984/Icryptian/releases) en GitHub.
2.  Descarga el archivo `.exe` de la última versión.
3.  Coloca el archivo en una carpeta de tu elección.
4.  Ejecutalo haciendo doble click o desde una consola.
5.  ¡Y listo! ya puedes encriptar y desencriptar archivos.

**Adicional**: Si deseas que puedas encriptar desde cualquier lugar sin tener que ejecutar el archivo, puedes hacerlo agregandolo a tu PATH:
1. **Comandos** (En PowerShell):
```powershell
$env:PATH += ";C:\ruta\a\la\carpeta"
```


2. **Manual**:
   1. Abre el menú Inicio, escribe "env" y selecciona "Editar las variables de entorno del sistema".

   2. Haz clic en el botón "Variables de entorno…".

   3. En la sección "Variables del sistema", (o "Variables de esta cuenta") busca la variable llamada "Path" y haz clic en "Editar".

   4. En la ventana que aparece, haz clic en "Nuevo" y añade la ruta completa de la carpeta donde está tu ejecutable.

   5. Confirma todas las ventanas con "Aceptar" para guardar los cambios.

   6. Reinicia cualquier consola de comandos abierta para que reconozca los cambios.

## Uso

La herramienta funciona con tres comandos principales: `genkey`, `encrypt` y `decrypt`.

### Generar una Clave (para Cifrado por Sustitución y Homofónico)

Antes de usar el cifrado por sustitución o homofónico, necesitas generar un archivo de clave:

```sh
icryptian genkey substitution
icryptian genkey homophonic
```

Esto creará un archivo `subst.key` en tu directorio actual.

### Encriptar un archivo

```sh
icryptian encrypt <ruta_del_archivo> --cipher <tipo_de_cifrado> [opciones]
```

Al encriptar, el archivo de salida tendrá el mismo nombre que el original, pero con la extensión `.ic` (por ejemplo, `mi_secreto.txt` se convertirá en `mi_secreto.ic`).

- `--cipher caesar`: Usa el Cifrado César. Requiere la opción `--shift`.
- `--cipher substitution`: Usa el Cifrado por Sustitución. Requiere un archivo `subst.key`.
- `--cipher transposition`: Usa el Cifrado por Transposición. Requiere la opción `--shift` (que actúa como clave).
- `--cipher vigenere`: Usa el Cifrado Vigenère. Requiere la opción `--key`.
- `--cipher binario`: Usa el Cifrado Binario. No requiere opciones adicionales.
- `--cipher homophonic`: Usa el Cifrado Homofónico. Requiere un archivo `homofonico.key`.

**Ejemplos:**
```sh
# Cifrado César
icryptian encrypt mi_secreto.txt --cipher caesar --shift 3

# Cifrado por Sustitución
icryptian encrypt mi_secreto.txt --cipher substitution

# Cifrado por Transposición
icryptian encrypt mi_secreto.txt --cipher transposition --shift 8

# Cifrado Vigenère
icryptian encrypt mi_secreto.txt --cipher vigenere --key "LEMON"

# Cifrado Binario
icryptian encrypt mi_secreto.txt --cipher binario

# Cifrado Homofónico
icryptian encrypt mi_secreto.txt --cipher homophonic
```

### Desencriptar un archivo

```sh
icryptian decrypt <ruta_del_archivo> --cipher <tipo_de_cifrado> [opciones]
```

El archivo encriptado ahora tendrá la extensión `.ic`. Al desencriptarlo, se generará un archivo con el nombre original pero sin extensión.

**Ejemplos:**
```sh
# Cifrado César
icryptian decrypt mi_secreto.ic --cipher caesar --shift 3

# Cifrado por Sustitución
icryptian decrypt mi_secreto.ic --cipher substitution

# Cifrado por Transposición
icryptian decrypt mi_secreto.ic --cipher transposition --shift 8

# Cifrado Vigenère
icryptian decrypt mi_secreto.ic --cipher vigenere --key "LEMON"

# Cifrado Binario
icryptian decrypt mi_secreto.ic --cipher binario

# Cifrado Homofónico
icryptian decrypt mi_secreto.ic --cipher homophonic
```

## Pruebas

Para ejecutar la suite de tests, clona el repositorio y ejecuta el siguiente comando desde la raíz del proyecto:

```sh
python -m unittest discover tests
```
