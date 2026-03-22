# Windows Setup Guide 🪟

Guía para configurar `video-downloader-library` en Windows.

## 1. Instalar Python

### Opción A: Desde python.org (Recomendado)

1. Ve a [python.org](https://www.python.org/downloads/)
2. Descarga Python 3.10 o superior
3. **IMPORTANTE:** Marca "Add Python to PATH" durante instalación
4. Click "Install Now"

### Opción B: Desde Microsoft Store

1. Abre Microsoft Store
2. Busca "Python"
3. Instala Python de Python Software Foundation

### Opción C: Desde Chocolatey (si tienes)

```cmd
choco install python
```

## 2. Verificar Instalación

Abre PowerShell o Command Prompt:

```cmd
python --version
pip --version
```

Deberías ver algo como:
```
Python 3.11.0
pip 23.0.1
```

## 3. Instalar Git (Opcional pero Recomendado)

1. Descarga desde [git-scm.com](https://git-scm.com/)
2. Ejecuta el instalador
3. Haz click "Next" en todas las pantallas

Verifica:
```cmd
git --version
```

## 4. Descargar el Proyecto

### Opción A: Con Git

```cmd
git clone https://github.com/tu-usuario/video-downloader-library.git
cd video-downloader-library
```

### Opción B: Manual

1. Descarga ZIP from GitHub
2. Extrae la carpeta
3. Abre PowerShell en esa carpeta

## 5. Crear Virtual Environment

En la carpeta del proyecto, ejecuta:

```cmd
python -m venv venv
```

### Activar Virtual Environment

```cmd
# En PowerShell
venv\Scripts\Activate.ps1

# En Command Prompt
venv\Scripts\activate.bat
```

**Nota:** Si obtienes error de ejecución en PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 6. Instalar la Librería

```cmd
pip install -r requirements.txt
```

O en modo desarrollo:

```cmd
pip install -e .
```

Con dependencias de desarrollo:

```cmd
pip install -e ".[dev]"
```

## 7. Instalar ffmpeg (Opcional)

### Opción A: Chocolatey (Más fácil)

```cmd
choco install ffmpeg
```

### Opción B: Manual

1. Descarga desde [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extrae en `C:\ffmpeg`
3. Agrega a PATH:
   - Windows + Pause/Break
   - "Advanced system settings"
   - Environment Variables
   - Agrega `C:\ffmpeg\bin` a PATH

### Opción C: Windows Package Manager

```cmd
winget install ffmpeg
```

Verifica:
```cmd
ffmpeg -version
```

## 8. Verificar Instalación

```cmd
python -c "from video_downloader_library import VideoDownloader; print('✅ OK')"
```

Si funciona, estás listo!

## 9. Tu Primer Script

Crea archivo `download.py`:

```python
from video_downloader_library import VideoDownloader

def on_progress(pct, filename, downloaded, total, speed):
    speed_mb = speed / (1024 * 1024)
    print(f"[{pct*100:5.1f}%] @ {speed_mb:.1f} MB/s")

def on_state(state):
    print(f"Estado: {state}")

downloader = VideoDownloader(None, on_progress, on_state, print)
downloader.download("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "720p", False)

import time
while downloader.is_downloading():
    time.sleep(1)
```

Ejecuta:

```cmd
python download.py
```

## 10. Ejecutar Ejemplos

```cmd
python examples/basic_usage.py
```

## Troubleshooting Windows 🔧

### Error: "Python is not recognized"

1. Reinstala Python
2. **IMPORTANTE:** Marca "Add Python to PATH"
3. Reinicia la terminal

### Error: "No module named 'yt_dlp'"

```cmd
pip install yt-dlp
```

### Error en PowerShell ejecutando comandos

Cambia a Command Prompt:

```cmd
# En lugar de:
venv\Scripts\Activate.ps1

# Usa:
venv\Scripts\activate.bat
```

### Permission Denied

Ejecuta PowerShell como "Run as administrator"

### pip.exe no encontrada

```cmd
python -m pip install --upgrade pip
```

### Virtual environment no funciona

```cmd
# Borra y recrea
rmdir /s venv
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Descargas por Defecto

Por defecto, los videos se descargan en tu carpeta actual.

Para cambiar la ubicación, edita `config.py` o usa:

```python
from video_downloader_library.config import DownloaderConfig

config = DownloaderConfig(
    download_path="C:\\Users\\TuUsuario\\Downloads"
)
```

## Archivos Importantes en Windows

- Python: `C:\Users\tu-usuario\AppData\Local\Programs\Python\Python311`
- Carpeta de usuario: `C:\Users\tu-usuario`
- Descargas: `C:\Users\tu-usuario\Downloads`

## Antivirus y Firewall

Si tienes problemas descargando:

1. Agrega Python a exclusiones del antivirus
2. Verifica firewall no bloquee conexiones

## Tips para Windows 🎯

1. **Usa Windows Terminal** - Es mejor que CMD
   - Descarga desde Microsoft Store
   
2. **Usa PowerShell Core** - Más moderno que PowerShell
   ```cmd
   choco install powershell-core
   ```

3. **Usa VSCode** - Para editar código
   ```cmd
   choco install vscode
   ```

4. **Ejecuta como administrador** - Si tienes permisos
   - Haz click derecho → "Run as administrator"

## Siguiente Paso 🚀

1. Crea cuenta en [GitHub](https://github.com)
2. Lee [GITHUB_SETUP.md](GITHUB_SETUP.md)
3. Sube tu proyecto a GitHub
4. ¡Comparte tu librería con el mundo!

## Recursos

- [Python Documentation](https://docs.python.org)
- [Virtual Environments Tutorial](https://docs.python.org/3/tutorial/venv.html)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/)

---

¿Problemas? Abre un issue en GitHub o revisa la documentación en README.md

Happy coding! 💻
