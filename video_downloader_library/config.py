"""Módulo de configuración para la librería de descarga de videos.

Define las opciones de configuración global que se pueden personalizar.
"""
import os
from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class DownloaderConfig:
    """Configuración para el descargador de videos.
    
    Attributes:
        download_path (str): Ruta donde guardar los videos descargados.
            Por defecto es el directorio actual.
        default_quality (str): Calidad por defecto para descargas:
            "best", "720p", "360p", "high_audio", "low_audio".
        write_subtitles (bool): Si descargar subtítulos por defecto.
        subtitle_langs (List[str]): Idiomas de subtítulos a descargar.
        socket_timeout (int): Timeout en segundos para conexiones de red.
        max_retries (int): Número máximo de reintentos en caso de error.
        quiet (bool): Si mostrar mensajes de yt-dlp.
        no_warnings (bool): Si mostrar advertencias de yt-dlp.
        log_file (Optional[str]): Archivo para guardar logs. None para no guardar.
        extra_ydl_opts (Dict[str, Any]): Opciones adicionales para yt-dlp.
    \"\"\"\n
    download_path: str = os.getcwd()
    default_quality: str = "720p"
    write_subtitles: bool = False
    subtitle_langs: List[str] = None
    socket_timeout: int = 60
    max_retries: int = 3
    quiet: bool = False
    no_warnings: bool = True
    log_file: Optional[str] = None
    extra_ydl_opts: Dict[str, Any] = None
    
    def __post_init__(self):
        """Inicializar valores por defecto después de dataclass init."""
        if self.subtitle_langs is None:
            self.subtitle_langs = ["es", "en"]
        if self.extra_ydl_opts is None:
            self.extra_ydl_opts = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir configuración a diccionario.
        
        Returns:
            Diccionario con todas las configuraciones.
        """
        return {
            "download_path": self.download_path,
            "default_quality": self.default_quality,
            "write_subtitles": self.write_subtitles,
            "subtitle_langs": self.subtitle_langs,
            "socket_timeout": self.socket_timeout,
            "max_retries": self.max_retries,
            "quiet": self.quiet,
            "no_warnings": self.no_warnings,
            "log_file": self.log_file,
            "extra_ydl_opts": self.extra_ydl_opts,
        }


# Instancia global de configuración
DEFAULT_CONFIG = DownloaderConfig()
