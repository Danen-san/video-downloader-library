# 🚀 Quick Start Guide

Comienza a usar `video-downloader-library` en 5 minutos.

## 1️⃣ Instalación Rápida

### Opción A: Instalación desde GitHub (Desarrollo)

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/video-downloader-library.git
cd video-downloader-library

# Ejecutar script de configuración (Linux/Mac)
chmod +x setup.sh
./setup.sh

# O instalación manual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Opción B: Desde PyPI (cuando se publique)

```bash
pip install video-downloader-library
```

## 2️⃣ Tu Primer Script

```python
from video_downloader_library import VideoDownloader

# Callbacks para monitorear progreso
def on_progress(pct, filename, downloaded, total, speed):
    speed_mb = speed / (1024 * 1024)
    print(f"[{pct*100:5.1f}%] {filename} @ {speed_mb:.1f} MB/s")

def on_state(state):
    print(f"→ {state}")

def on_error(error):
    print(f"❌ {error}")

# Crear descargador
downloader = VideoDownloader(None, on_progress, on_state, on_error)

# Descargar video
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
downloader.download(url, quality="720p", write_subtitles=True)

# Esperar a que termine
import time
while downloader.is_downloading():
    time.sleep(1)
```

Guarda como `download.py` y ejecuta:
```bash
python download.py
```

## 3️⃣ Obtener Información del Video

```python
from video_downloader_library import fetch_video_info

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
info = fetch_video_info(url)

print(f"Título: {info['title']}")
print(f"Duración: {info['duration']}s")
print(f"Tamaños:")
for quality, size in info['sizes'].items():
    print(f"  {quality}: {size}")
```

## 4️⃣ Control de Pausa/Cancelación

```python
import time
from video_downloader_library import VideoDownloader

downloader = VideoDownloader(None, print, print, print)
downloader.download("https://youtube.com/watch?v=...", "720p", False)

# Pausar después de 5 segundos
time.sleep(5)
downloader.pause()
print("⏸️ Pausado")

# Esperar
time.sleep(3)

# Reanudar
downloader.resume()
print("▶️ Reanudado")

# Esperar a que termine
while downloader.is_downloading():
    time.sleep(1)
```

## 5️⃣ Configuración Personalizada

```python
from video_downloader_library import VideoDownloader
from video_downloader_library.config import DownloaderConfig

# Crear configuración
config = DownloaderConfig(
    download_path="/home/user/Videos",
    default_quality="best",
    write_subtitles=True,
    subtitle_langs=["es", "en"]
)

# Tu descargador con esta configuración
downloader = VideoDownloader(None, print, print, print)
# Luego usa: downloader.download(...)
```

## 📚 Documentación Completa

Para aprender más:

- **README.md** - Guía completa con todos los detalles
- **RESUMEN.md** - Resumen de mejoras implementadas
- **examples/basic_usage.py** - 5 ejemplos ejecutables
- **GITHUB_SETUP.md** - Cómo subir a GitHub

## 🎯 Calidades Disponibles

| Calidad | Descripción | Ejemplo |
|---------|------------|---------|
| `best` | Mejor calidad (máx 1080p) | 1080p + audio |
| `720p` | HD estándar | 720p (60-130MB) |
| `360p` | Bajo (móvil) | 360p (10-30MB) |
| `high_audio` | Audio de calidad | ~5MB/min |
| `low_audio` | Audio comprimido | ~1MB/min |

## ⚠️ Requisitos

- Python 3.8+
- yt-dlp >= 2024.1.1
- ffmpeg (opcional pero recomendado)

**Instalar ffmpeg:**

Linux:
```bash
sudo apt-get install ffmpeg
```

macOS:
```bash
brew install ffmpeg
```

Windows:
```bash
choco install ffmpeg
```

## 🔧 Troubleshooting

### Error: "No module named 'yt_dlp'"
```bash
pip install yt-dlp
```

### Video no se descarga
1. Verifica internet y URL
2. Intenta sin subtítulos
3. Actualiza yt-dlp: `pip install --upgrade yt-dlp`

### Permisos denegados
```bash
# Asignar permisos a carpeta de descargas
chmod 755 ~/Videos
```

## 📞 Necesitas Ayuda?

- Lee [README.md](README.md)
- Ve [ejemplos](examples/basic_usage.py)
- Abre un [issue](https://github.com/tu-usuario/video-downloader-library/issues)

## 🎉 ¡Listo!

Eso es todo. Ahora puedes descargar videos. ¿Qué esperas?

```bash
python download.py
```

---

**Pro tip:** Usa la librería en tus scripts para automatizar descargas masivas.

Happy downloading! 🚀
