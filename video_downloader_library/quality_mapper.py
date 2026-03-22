"""Módulo para mapeo de calidades a formatos de yt-dlp.

Define las opciones de calidad disponibles y las convierte a selectores
de formato válidos para yt-dlp. Soporta video en diferentes resoluciones
y audio en alta/baja calidad.

Calidades soportadas:
    - best: Mejor calidad disponible (máx. 1080p)
    - 720p: Video HD 720p
    - 360p: Video de baja resolución
    - high_audio: Audio de alta calidad
    - low_audio: Audio de baja calidad

Ejemplo:
    >>> format_str = get_format_selector("720p")
    >>> print(format_str)
    best[ext=mp4][height<=720]
"""
from typing import Dict


def get_format_selector(quality: str) -> str:
    """Obtener selector de formato para yt-dlp según calidad especificada.
    
    Convierte nombres de calidad legibles a selectores de formato válidos
    que yt-dlp puede procesar.
    
    Args:
        quality: Nombre de la calidad deseada.
        
    Returns:
        String con la especificación de formato para yt-dlp.
        
    Raises:
        ValueError: Si la calidad no está soportada.
        
    Example:
        >>> selector = get_format_selector("720p")
        >>> # Usar con yt-dlp
        >>> ydl_opts = {"format": selector}
    """
    quality_map: Dict[str, str] = {
        "best": "best[ext=mp4][height<=1080]",
        "720p": "best[ext=mp4][height<=720]",
        "360p": "best[ext=mp4][height<=360]",
        "high_audio": "bestaudio[ext=m4a]",
        "low_audio": "worstaudio[ext=m4a]",
    }
    if quality not in quality_map:
        raise ValueError(
            f"Calidad no soportada: {quality}. Opciones válidas: best, 720p, 360p, high_audio, low_audio"
        )
    return quality_map[quality]