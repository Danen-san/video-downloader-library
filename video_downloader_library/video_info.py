"""Módulo para obtener información de videos sin descargarlos.

Extrae metadatos útiles como título, duración, tamaños por calidad,
thumbnails y formatos disponibles. Utiliza yt-dlp para acceder a
información sin realizar descargas.

Ejemplo:
    >>> info = fetch_video_info("https://youtube.com/watch?v=abc")
    >>> print(info["title"])
    >>> print(info["duration"])
    >>> print(info["sizes"])
"""
from typing import Dict, Any

import yt_dlp

from quality_mapper import get_format_selector


def fetch_video_info(url: str) -> Dict[str, Any]:
    """Extraer información de video sin descargarlo.
    
    Obtiene metadatos útiles del video incluyendo título, duración,
    thumbnail y tamaños estimados para cada calidad de descarga.
    
    Args:
        url: URL del video (YouTube, Vimeo, etc.).
        
    Returns:
        Diccionario con claves:
            - title (str): Título del video
            - duration (int): Duración en segundos
            - thumbnail (str): URL de la miniatura
            - sizes (dict): Tamaño estimado por calidad (e.g., {"720p": "150.5MB"})
            
    Note:
        Retorna valores por defecto con "?MB" si no puede calcular el tamaño.
        La duración está en segundos.
        
    Example:
        >>> info = fetch_video_info("https://youtube.com/watch?v=dQw4w9WgXcQ")
        >>> print(f"Título: {info['title']}")
        >>> print(f"Duración: {info['duration']}s")
        >>> print(f"Tamaños: {info['sizes']}")
    """
    quality_keys = ["best", "720p", "360p", "high_audio", "low_audio"]

    try:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "extract_flat": False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        title = info.get("title", "Título desconocido")
        duration = info.get("duration", 0)
        thumbnail = info.get("thumbnail", "")
        formats = info.get("formats", [])

        def get_size_for_quality(quality_key: str) -> str:
            try:
                format_selector = get_format_selector(quality_key)
                temp_ydl_opts = {"format": format_selector, "quiet": True}
                with yt_dlp.YoutubeDL(temp_ydl_opts) as temp_ydl:
                    selected_formats = temp_ydl._select_formats(info)
                    if not selected_formats:
                        return "?MB"
                    selected_fmt = selected_formats[0]

                size_approx = selected_fmt.get('filesize_approx')
                if not size_approx:
                    if selected_fmt.get('filesize'):
                        size_approx = selected_fmt['filesize']
                    elif selected_fmt.get('filesize_approx'):
                        size_approx = selected_fmt['filesize_approx']

                if not size_approx:
                    for f in formats:
                        if f.get('format_id') == selected_fmt.get('format_id'):
                            if f.get('filesize'):
                                size_approx = f['filesize']
                                break
                            elif f.get('filesize_approx'):
                                size_approx = f['filesize_approx']
                                break

                if size_approx and isinstance(size_approx, (int, float)) and size_approx > 0:
                    size_mb = size_approx / (1024 * 1024)
                    return f"{size_mb:.1f}MB"
                else:
                    return "?MB"

            except Exception:
                return "?MB"

        sizes = {key: get_size_for_quality(key) for key in quality_keys}

        return {
            "title": title,
            "duration": duration,
            "thumbnail": thumbnail,
            "sizes": sizes
        }

    except Exception:
        return {
            "title": "Error al cargar el video",
            "duration": 0,
            "thumbnail": "",
            "sizes": {key: "?MB" for key in quality_keys}
        }