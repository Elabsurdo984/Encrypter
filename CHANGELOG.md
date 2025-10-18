# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.4.0] - 2025-10-18

### Changed
- La extensión de los archivos encriptados ahora es `.ic`.
- Al encriptar, se elimina la extensión original del archivo. Por ejemplo, `archivo.txt` se convierte en `archivo.ic`.
- Al desencriptar, el archivo de salida no tiene extensión. Por ejemplo, `archivo.ic` se convierte en `archivo`.

## [1.3.0] - 2025-10-20

### Changed
- Se cambio el nombre de la aplicación a Icryptian

## [1.2.0] - 2025-10-18

### Added

- Implementación de Cifrado por Transposición.

## [1.1.0] - 2025-10-17

### Added

- Implementación de Cifrado por Sustitución.
- Comando `genkey` para generar claves de sustitución.

### Changed

- Refactorización del CLI para soportar múltiples cifrados con el argumento `--cipher`.
- Actualización de la documentación y el versionado.

## [1.0.0] - 2025-10-17

### Added

- Lanzamiento inicial de CliEnDecrypter.
- Implementación de Cifrado César para encriptar y desencriptar archivos.
- Creación de un ejecutable (`.exe`) con PyInstaller.
- Script de instalación `install.bat` para facilitar la instalación en Windows.
- Documentación inicial (`README.md`) y `CHANGELOG.md`.
