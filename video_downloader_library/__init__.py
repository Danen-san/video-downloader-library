"""yt-dlp Video Downloader Library.

Una librería personalizada para descargar videos desde YouTube y otras plataformas
soportadas por yt-dlp con control avanzado de pausa, cancelación y múltiples opciones
de calidad.

Módulos Principales:
    - VideoDownloader: Clase principal para descargas con control de estado
    - fetch_video_info: Obtener información de videos sin descargar
    - get_format_selector: Mapeo de calidades a formatos de yt-dlp
    
Ejemplo de Uso:
    >>> from video_downloader_library import VideoDownloader, fetch_video_info
    >>>
    >>> # Obtener información del video
    >>> info = fetch_video_info("https://youtube.com/watch?v=...")
    >>> print(f"Título: {info['title']}")
    >>> print(f"Tamaños disponibles: {info['sizes']}")
    >>>
    >>> # Descargar video
    >>> def on_progress(pct, fname, down, total, speed):
    ...     print(f"Descargando {fname}: {pct*100:.1f}%")
    ...
    >>> def on_state(state):
    ...     print(f"Estado: {state}")
    ...
    >>> def on_error(error):
    ...     print(f"Error: {error}")
    ...
    >>> downloader = VideoDownloader(None, on_progress, on_state, on_error)
    >>> downloader.download("https://youtube.com/watch?v=...", "720p", True)

Atributos:
    VERSION (str): Versión de la librería
    __author__ (str): Autor
    __email__ (str): Email de contacto
"""

from .video_dowloader import VideoDownloader
from .video_info import fetch_video_info
from .quality_mapper import get_format_selector

__version__ = "1.0.0"
__author__ = "Tu Nombre"
__email__ = "tu.email@example.com"

__all__ = [
    "VideoDownloader",
    "fetch_video_info",
    "get_format_selector",
    "__version__",
    "__author__",
    "__email__",
]
