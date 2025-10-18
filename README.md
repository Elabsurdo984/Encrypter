# Icryptian

Una sencilla herramienta de línea de comandos (CLI) para encriptar y desencriptar archivos utilizando cifrados clásicos. Creado en Python.

## Características

- **Cifrado César**: Encripta y desencripta archivos de texto.
- **Cifrado por Sustitución**: Utiliza un alfabeto desordenado como clave.
- **Cifrado por Transposición**: Cambia la posición de los caracteres usando una clave numérica.
- **Empaquetado**: Se distribuye como un único ejecutable de Windows (`.exe`).
- **Instalador simple**: Incluye un script `install.bat` para una instalación automática en Windows (copia el archivo y lo añade al PATH).

## Instalación

Para instalar `Icryptian` en tu sistema, sigue estos pasos:

1.  Ve a la sección de [Releases](https://github.com/Elabsurdo984/Icryptian/releases) en GitHub.
2.  Descarga el archivo `.zip` de la última versión.
3.  Descomprime el archivo en una carpeta de tu elección.
4.  Haz doble clic en el archivo `install.bat`. Esto instalará el ejecutable y lo añadirá automáticamente a tu PATH de usuario.
5.  Cierra y vuelve a abrir cualquier terminal (CMD, PowerShell, etc.) para que los cambios se apliquen.

¡Listo! Ahora puedes usar el comando `icryptian` desde cualquier lugar.

## Uso

La herramienta funciona con tres comandos principales: `genkey`, `encrypt` y `decrypt`.

### Generar una Clave (para Cifrado por Sustitución)

Antes de usar el cifrado por sustitución, necesitas generar un archivo de clave:

```sh
icryptian genkey substitution
```

Esto creará un archivo `subst.key` en tu directorio actual.

### Encriptar un archivo

```sh
icryptian encrypt <ruta_del_archivo> --cipher <tipo_de_cifrado> [opciones]
```

- `--cipher caesar`: Usa el Cifrado César. Requiere la opción `--shift`.
- `--cipher substitution`: Usa el Cifrado por Sustitución. Requiere un archivo `subst.key`.
- `--cipher transposition`: Usa el Cifrado por Transposición. Requiere la opción `--shift` (que actúa como clave).

**Ejemplos:**
```sh
# Cifrado César
icryptian encrypt mi_secreto.txt --cipher caesar --shift 3

# Cifrado por Sustitución
icryptian encrypt mi_secreto.txt --cipher substitution

# Cifrado por Transposición
icryptian encrypt mi_secreto.txt --cipher transposition --shift 8
```

### Desencriptar un archivo

```sh
icryptian decrypt <ruta_del_archivo> --cipher <tipo_de_cifrado> [opciones]
```

**Ejemplos:**
```sh
# Cifrado César
icryptian decrypt mi_secreto.txt.caesar --cipher caesar --shift 3

# Cifrado por Sustitución
icryptian decrypt mi_secreto.txt.substitution --cipher substitution

# Cifrado por Transposición
icryptian decrypt mi_secreto.txt.transposition --cipher transposition --shift 8
```
