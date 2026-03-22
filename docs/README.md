# Video Downloader Library 📹

Una librería personalizada y robusta para descargar videos desde YouTube y otras plataformas soportadas por [yt-dlp](https://github.com/yt-dlp/yt-dlp), con control avanzado de pausa, cancelación y múltiples opciones de calidad.

## Características ✨

- ✅ **Descarga de videos** desde YouTube, Vimeo, Twitter y cientos de sitios más
- ⏸️ **Control de pausa/reanudación** - Pausar y reanudar descargas en cualquier momento
- ❌ **Cancelación segura** - Cancelar descargas sin dejar archivos corruptos
- 📊 **Monitoreo en tiempo real** - Callbacks para progreso, velocidad y estado
- 🎬 **Múltiples calidades** - best, 720p, 360p, high_audio, low_audio
- 📝 **Subtítulos automáticos** - Descarga subtítulos en español e inglés
- 🚀 **Hilos separados** - No bloquea la interfaz de usuario
- ⚙️ **Altamente configurable** - Personaliza rutas, calidades, timeouts, etc.

## Instalación 📦

### Desde GitHub (desarrollo)

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/video-downloader-library.git
cd video-downloader-library

# Instalar en modo desarrollo
pip install -e .

# O instalar solo dependencias
pip install -r requirements.txt
```

### Desde PyPI (cuando se publique)

```bash
pip install video-downloader-library
```

## Requisitos

- Python 3.8 o superior
- yt-dlp >= 2024.1.1
- ffmpeg (opcional, pero recomendado para convertir formatos)

### Instalar ffmpeg

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Descargar desde [ffmpeg.org](https://ffmpeg.org/download.html) o:
```bash
choco install ffmpeg
```

## Uso Rápido 🚀

### Ejemplo básico

```python
from video_downloader_library import VideoDownloader

# Definir callbacks
def on_progress(pct, filename, downloaded, total, speed):
    speed_mb = speed / (1024 * 1024)
    total_mb = total / (1024 * 1024)
    downloaded_mb = downloaded / (1024 * 1024)
    print(f"{filename}: {pct*100:.1f}% "
          f"({downloaded_mb:.1f}/{total_mb:.1f} MB) "
          f"@ {speed_mb:.1f} MB/s")

def on_state(state):
    print(f"Estado: {state}")

def on_error(error):
    print(f"Error: {error}")

# Crear descargador
downloader = VideoDownloader(None, on_progress, on_state, on_error)

# Descargar video
url = "https://www.youtube.com/watch?v=..."
downloader.download(url, quality="720p", write_subtitles=True)
```

### Obtener información del video

```python
from video_downloader_library import fetch_video_info

info = fetch_video_info("https://www.youtube.com/watch?v=...")

print(f"Título: {info['title']}")
print(f"Duración: {info['duration']} segundos")
print(f"Miniatura: {info['thumbnail']}")
print(f"Tamaños disponibles:")
for quality, size in info['sizes'].items():
    print(f"  {quality}: {size}")
```

### Control de pausa y cancelación

```python
import time
from video_downloader_library import VideoDownloader

def on_progress(pct, fname, down, total, speed):
    print(f"Progreso: {pct*100:.1f}%")

downloader = VideoDownloader(None, on_progress, None, None)

# Iniciar descarga
downloader.download("https://youtube.com/watch?v=...", "720p", False)

# Esperar 5 segundos y pausar
time.sleep(5)
if downloader.is_downloading():
    downloader.pause()
    print("Descarga pausada")
    
    # Esperar 3 segundos
    time.sleep(3)
    
    # Reanudar
    downloader.resume()
    print("Descarga reanudada")
```

## Configuración Avanzada ⚙️

```python
from video_downloader_library import VideoDownloader
from video_downloader_library.config import DownloaderConfig

# Crear configuración personalizada
config = DownloaderConfig(
    download_path="/home/user/Videos",
    default_quality="best",
    write_subtitles=True,
    subtitle_langs=["es", "en", "fr"],
    socket_timeout=120,
    max_retries=5,
    no_warnings=False,
    log_file="/tmp/downloader.log"
)

# Usar configuración en descargador
downloader = VideoDownloader(
    None,
    on_progress=print,
    state_callback=print,
    error_callback=print
)
```

## Calidades Disponibles

| Calidad | Descripción |
|---------|------------|
| `best` | Mejor calidad disponible (máximo 1080p) |
| `720p` | Video HD 720p |
| `360p` | Video de baja resolución (móvil) |
| `high_audio` | Audio de alta calidad (FLAC/AAC) |
| `low_audio` | Audio de baja calidad (para ahorrar espacio) |

## Estructura del Proyecto 📂

```
video-downloader-library/
├── video_downloader_library/
│   ├── __init__.py              # Módulo principal
│   ├── video_dowloader.py       # Clase VideoDownloader
│   ├── video_info.py            # Función fetch_video_info
│   ├── quality_mapper.py        # Mapeo de calidades
│   ├── exceptions.py            # Excepciones personalizadas
│   └── config.py                # Configuración
├── setup.py                     # Configuración de setuptools
├── requirements.txt             # Dependencias
├── README.md                    # Este archivo
├── .gitignore                   # Archivos a ignorar en Git
└── examples/
    └── basic_usage.py           # Ejemplos de uso
```

## Manejo de Errores 🛡️

La librería usa excepciones personalizadas para diferentes tipos de errores:

```python
from video_downloader_library import VideoDownloader
from video_downloader_library.exceptions import (
    InvalidQualityError,
    InvalidURLError,
    DownloadError,
    VideoInfoError
)

try:
    downloader.download(url, "720p", False)
except InvalidQualityError:
    print("Calidad no soportada")
except InvalidURLError:
    print("URL inválida o no soportada")
except DownloadError:
    print("Error durante la descarga")
except Exception as e:
    print(f"Error inesperado: {e}")
```

## API Reference 📚

### VideoDownloader

**Constructor:**
```python
VideoDownloader(
    page: Optional[object],
    progress_callback: Callable,
    state_callback: Callable,
    error_callback: Callable
)
```

**Métodos:**
- `download(url: str, quality: str, write_subtitles: bool) -> None` - Descargar video
- `pause() -> None` - Pausar descarga
- `resume() -> None` - Reanudar descarga
- `cancel() -> None` - Cancelar descarga
- `is_downloading() -> bool` - Verificar si hay descarga activa
- `is_paused() -> bool` - Verificar si está pausada

### fetch_video_info

```python
def fetch_video_info(url: str) -> Dict[str, Any]
```

Retorna diccionario con:
- `title` (str): Título del video
- `duration` (int): Duración en segundos
- `thumbnail` (str): URL de la miniatura
- `sizes` (dict): Tamaños por calidad

### get_format_selector

```python
def get_format_selector(quality: str) -> str
```

Obtiene el selector de formato para yt-dlp.

## Troubleshooting 🔧

### "ModuleNotFoundError: No module named 'yt_dlp'"

```bash
pip install yt-dlp
```

### Videos no se descargan

1. Verifica que tienes internet
2. Verifica que la URL es correcta
3. Intenta con `no_warnings=False` para ver mensajes de yt-dlp
4. Actualiza yt-dlp: `pip install --upgrade yt-dlp`

### Subtítulos no funcionan

```bash
# Algunos idiomas requieren códigos específicos
# Usa el código ISO 639-1 (es, en, fr, de, etc.)
subtitle_langs=["es", "en"]
```

### Errores de permisos en directorio

```python
import os
# Asignar permisos de escritura
os.makedirs("/ruta/a/videos", mode=0o755, exist_ok=True)
```

## Contribuir 🤝

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea un branch para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia 📄

Este proyecto está bajo la licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

## Autores ✍️

- **Tu Nombre** - [tu.correo@example.com](mailto:tu.correo@example.com)

## Créditos 🙏

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - El poder detrás de las descargas
- [youtube-dl](https://github.com/ytdl-org/youtube-dl) - Predecesor

## Changelog 📝

### v1.0.0 (2024-03-19)
- ✅ Primera versión estable
- ✅ Soporte para pausa/reanudación
- ✅ Control de cancelación
- ✅ Múltiples calidades
- ✅ Subtítulos automáticos
- ✅ Documentación completa

## Roadmap 🗺️

- [ ] Descargar listas de reproducción
- [ ] Búsqueda de videos
- [ ] Caché de metadatos
- [ ] GUI con PyQt
- [ ] Integración con webhooks
- [ ] Soporte para proxies
- [ ] Descarga en paralelo de múltiples videos

## FAQ ❓

**P: ¿Puedo descargar videos privados?**
R: No, solo videos públicos que yt-dlp pueda acceder.

**P: ¿Es legal descargar videos?**
R: Depende de los términos de servicio del sitio y las leyes locales. Usa responsablemente.

**P: ¿Puedo usar esto comercialmente?**
R: Sí, bajo la licencia MIT, pero respeta los derechos de autor del contenido.

**P: ¿Soporta descargas simultáneas?**
R: Actualmente no, pero está en el roadmap.

---

Para más información, issues o preguntas, visita [GitHub Issues](https://github.com/tu-usuario/video-downloader-library/issues).
