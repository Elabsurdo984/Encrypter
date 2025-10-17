# CliEnDecrypter

Una sencilla herramienta de línea de comandos (CLI) para encriptar y desencriptar archivos utilizando cifrados clásicos. Creado en Python.

## Características

- **Cifrado César**: Encripta y desencripta archivos de texto.
- **Empaquetado**: Se distribuye como un único ejecutable de Windows (`.exe`).
- **Instalador simple**: Incluye un script `install.bat` para una instalación automática en Windows (copia el archivo y lo añade al PATH).

## Instalación

Para instalar `CliEnDecrypter` en tu sistema, sigue estos pasos:

1.  Ve a la sección de [Releases](https://github.com/TU_USUARIO/TU_REPOSITORIO/releases) en GitHub.
2.  Descarga el archivo `.zip` de la última versión.
3.  Descomprime el archivo en una carpeta de tu elección.
4.  Haz doble clic en el archivo `install.bat`. Esto instalará el ejecutable y lo añadirá automáticamente a tu PATH de usuario.
5.  Cierra y vuelve a abrir cualquier terminal (CMD, PowerShell, etc.) para que los cambios se apliquen.

¡Listo! Ahora puedes usar el comando `encrypter` desde cualquier lugar.

## Uso

La herramienta funciona con dos comandos principales: `encrypt` y `decrypt`.

### Encriptar un archivo

```sh
encrypter encrypt <ruta_del_archivo> --shift <numero_de_desplazamiento>
```

- `<ruta_del_archivo>`: El archivo de texto que quieres encriptar.
- `<numero_de_desplazamiento>`: La clave para el cifrado César (un número entero).

**Ejemplo:**
```sh
encrypter encrypt mi_secreto.txt --shift 3
```
Esto creará un archivo llamado `mi_secreto.txt.cesar`.

### Desencriptar un archivo

```sh
encrypter decrypt <ruta_del_archivo_encriptado> --shift <numero_de_desplazamiento>
```

- `<ruta_del_archivo_encriptado>`: El archivo `.cesar` que quieres desencriptar.
- `<numero_de_desplazamiento>`: La misma clave que usaste para encriptar.

**Ejemplo:**
```sh
encrypter decrypt mi_secreto.txt.cesar --shift 3
```
Esto restaurará el archivo original `mi_secreto.txt`.
