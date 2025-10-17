@echo off
setlocal

:: --- Configuración ---
set "AppName=encrypter"
set "ExecutableName=encrypter.exe"
:: Usar AppData\Local para no requerir permisos de administrador
set "InstallDir=%LOCALAPPDATA%\%AppName%"

echo =================================================
echo   Instalador para %AppName%
echo =================================================
echo.
echo Este script instalara %ExecutableName% en tu sistema.
echo.
echo Directorio de instalacion: %InstallDir%
echo.
echo Se agregara esta carpeta a tu PATH de usuario.
echo.

:confirm
set /p "choice=¿Deseas continuar? (S/N): "
if /i "%choice%"=="S" goto :install
if /i "%choice%"=="N" goto :cancel
goto :confirm

:install
echo.
echo Creando directorio de instalacion...
if not exist "%InstallDir%" (
    mkdir "%InstallDir%"
)

echo.
echo Copiando archivos...
if not exist "%ExecutableName%" (
    echo Error: %ExecutableName% no se encuentra en la misma carpeta que este script.
    echo Asegurate de que 'encrypter.exe' y 'install.bat' esten juntos.
    pause
    exit /b 1
)
copy "%ExecutableName%" "%InstallDir%\"

echo.
echo Actualizando el PATH del usuario...
echo (Esto permite ejecutar '%AppName%' desde cualquier terminal)
echo.

:: Usar setx para añadir la ruta de forma permanente al PATH del usuario.
:: Se comprueba si la ruta ya existe para no duplicarla.
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path') do set "CURRENT_PATH=%%b"

echo "%CURRENT_PATH%" | find /i "%InstallDir%" >nul
if %errorlevel%==0 (
    echo La ruta ya existe en el PATH. No se necesita accion.
) else (
    echo Agregando la ruta al PATH...
    setx Path "%InstallDir%;%CURRENT_PATH%"
    echo.
    echo ¡PATH actualizado!
)

echo.
echo =================================================
echo   Instalacion completada.
echo =================================================
echo.
echo Por favor, CIERRA y VUELVE A ABRIR cualquier terminal
echo para que los cambios en el PATH surtan efecto.
echo.
echo Ahora puedes ejecutar '%AppName% --help' en una nueva terminal.
echo.
pause
goto :eof

:cancel
echo Instalacion cancelada.
pause
exit /b 0
