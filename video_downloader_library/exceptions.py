"""Excepciones personalizadas para la librería de descarga de videos.

Define excepciones específicas para diferentes tipos de errores que pueden
ocurrir durante la descarga y procesamiento de videos.
"""


class VideoDownloaderError(Exception):
    """Excepción base para todos los errores de la librería."""

    pass


class InvalidQualityError(VideoDownloaderError):
    """Se lanza cuando se especifica una calidad no soportada."""

    pass


class InvalidURLError(VideoDownloaderError):
    """Se lanza cuando la URL especificada es inválida o no es soportada."""

    pass


class DownloadError(VideoDownloaderError):
    """Se lanza cuando ocurre un error durante la descarga."""

    pass


class VideoInfoError(VideoDownloaderError):
    """Se lanza cuando no se puede obtener información del video."""

    pass


class DownloadCancelledError(VideoDownloaderError):
    """Se lanza cuando el usuario cancela una descarga en curso."""

    pass
