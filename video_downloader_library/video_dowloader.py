"""Módulo principal para descarga de videos con yt-dlp.

Proporciona la clase VideoDownloader con funcionalidades avanzadas de descarga
que incluyen:
- Pausa y reanudación de descargas
- Cancelación de descargas en curso
- Cálculo y seguimiento de velocidad de descarga
- Callbacks para progreso, estado y errores
- Soporte para subtítulos en múltiples idiomas
- Descarga en hilos separados para no bloquear la interfaz

Ejemplo:
    >>> def on_progress(pct, filename, downloaded, total, speed):
    ...     print(f"Progreso: {pct*100:.1f}%")
    ...
    >>> downloader = VideoDownloader(None, on_progress, None, None)
    >>> downloader.download("https://...", "720p", False)
"""
import os
import threading
import time
from typing import Callable, Optional

import yt_dlp

from quality_mapper import get_format_selector

DOWNLOAD_PATH = os.getcwd()

class VideoDownloader:
    """Clase para descargar videos desde plataformas soportadas por yt-dlp.
    
    Gestiona descargas de video con control total sobre pausa, reanudación y
    cancelación. Proporciona información en tiempo real del progreso mediante
    callbacks.
    
    Args:
        page: Objeto de página (opcional, para integración con UI).
        progress_callback: Función llamada durante la descarga con firma:
            (porcentaje: float, nombre_archivo: str, descargado: int, total: int, velocidad: float)
        state_callback: Función llamada al cambiar estado: "finished", "cancelled", "success".
        error_callback: Función llamada si ocurre un error con mensaje de error.
        
    Attributes:
        _paused (bool): Indica si la descarga está pausada.
        _cancelled (bool): Indica si la descarga fue cancelada.
        _is_downloading (bool): Indica si hay una descarga en curso.
        _current_ydl (Optional[yt_dlp.YoutubeDL]): Instancia actual de yt-dlp.
    
    Example:
        >>> def progress(pct, fname, down, total, speed):
        ...     print(f"{fname}: {pct*100:.1f}% a {speed/1024/1024:.1f}MB/s")
        >>> def state(s):
        ...     print(f"Estado: {s}")
        >>> def error(e):
        ...     print(f"Error: {e}")
        >>> dl = VideoDownloader(None, progress, state, error)
        >>> dl.download("https://example.com/video", "720p", True)
    """
    
    def __init__(
        self,
        page: Optional[object],
        progress_callback: Callable,
        state_callback: Callable,
        error_callback: Callable,
    ) -> None:
        """Inicializar VideoDownloader.
        
        Args:
            page: Referencia a página/ventana principal (puede ser None).
            progress_callback: Función para actualizar progreso.
            state_callback: Función para cambios de estado.
            error_callback: Función para manejar errores.
        """
        self.page = page
        self.progress_callback = progress_callback
        self.state_callback = state_callback
        self.error_callback = error_callback
        self._paused = False
        self._cancelled = False
        self._current_ydl = None
        self._start_time = None
        self._last_downloaded = 0
        self._last_time = None
        self._is_downloading = False

    def _progress_hook(self, d: dict) -> None:
        """Procesar eventos de progreso de yt-dlp.
        
        Llamado automáticamente por yt-dlp durante la descarga para reportar
        progreso. Calcula velocidad instantánea y maneja pausa/cancelación.
        
        Args:
            d: Diccionario con información de progreso de yt-dlp.
            
        Raises:
            Exception: Si la descarga fue cancelada por el usuario.
        """
        if self._cancelled:
            raise Exception("Descarga cancelada por el usuario")
            
        if self._paused:
            while self._paused and not self._cancelled:
                import time
                time.sleep(0.1)
        
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate") or 1
            downloaded = d.get("downloaded_bytes", 0)
            pct = downloaded / total if total > 0 else 0
            filename = d.get("info_dict", {}).get("filename", "...")
            
            # Calcular velocidad de descarga
            current_time = time.time()
            if not self._start_time:
                self._start_time = current_time
                self._last_downloaded = downloaded
                self._last_time = current_time
            
            # Calcular velocidad instantánea
            time_diff = current_time - self._last_time
            downloaded_diff = downloaded - self._last_downloaded
            
            if time_diff > 0:
                speed = downloaded_diff / time_diff  # bytes por segundo
            else:
                speed = 0
                
            self._last_downloaded = downloaded
            self._last_time = current_time
            
            self.progress_callback(pct, filename, downloaded, total, speed)

        elif d["status"] == "finished":
            self._is_downloading = False
            self.state_callback("finished")

        elif d["status"] == "error":
            self._is_downloading = False
            self.error_callback("Error durante la descarga")

    def pause(self) -> None:
        """Pausar la descarga en curso.
        
        La descarga se congelará hasta que se llame a resume().
        Los hooks de progreso continuarán comprobando este estado.
        """
        self._paused = True

    def resume(self) -> None:
        """Reanudar una descarga pausada.
        
        Restablece los timers de velocidad para evitar lecturas incorrectas.
        """
        self._paused = False
        # Reiniciar mediciones de velocidad al reanudar
        self._last_time = time.time()

    def cancel(self) -> None:
        """Cancelar la descarga en curso de forma segura.
        
        Detiene el proceso de descarga y limpia recursos.
        Es seguro llamarlo desde cualquier hilo.
        """
        self._cancelled = True
        self._paused = False
        self._is_downloading = False
        if self._current_ydl:
            try:
                self._current_ydl.cancel_download()
            except:
                pass

    def is_paused(self) -> bool:
        """Verificar si la descarga actual está pausada.
        
        Returns:
            True si la descarga está pausada, False en caso contrario.
        """
        return self._paused

    def is_downloading(self) -> bool:
        """Verificar si hay una descarga activa.
        
        Returns:
            True si hay una descarga sin terminar, False si terminó o no comenzó.
        """
        return self._is_downloading

    def download(self, url: str, quality: str, write_subtitles: bool) -> None:
        """Descargar video desde URL en calidad especificada.
        
        Inicia la descarga en un hilo separado para no bloquear la interfaz.
        Reporta progreso mediante callbacks registrados en el constructor.
        
        Args:
            url: URL del video a descargar (YouTube, etc.).
            quality: Calidad a descargar ("best", "720p", "360p", "high_audio", "low_audio").
            write_subtitles: Si True, descarga subtítulos en español e inglés.
            
        Raises:
            ValueError: Si la calidad especificada no es válida (reportado via error_callback).
        
        Example:
            >>> downloader.download("https://youtube.com/watch?v=abc", "720p", True)
        """
        # Reiniciar mediciones de velocidad
        self._start_time = None
        self._last_downloaded = 0
        self._last_time = None
        self._paused = False
        self._cancelled = False
        self._is_downloading = True
        
        # Mapeo de claves del dropdown a claves internas
        quality_key_map = {"highaudio": "high_audio", "lowaudio": "low_audio"}
        internal_quality = quality_key_map.get(quality, quality)

        try:
            format_str = get_format_selector(internal_quality)
        except ValueError as ve:
            self.error_callback(str(ve))
            return

        # Opciones para yt-dlp
        ydl_opts = {
            "format": format_str,
            "outtmpl": os.path.join(DOWNLOAD_PATH, "%(title)s.%(ext)s"),
            "noplaylist": True,
            "quiet": False,
            "no_warnings": True,
            "progress_hooks": [self._progress_hook],
        }

        if write_subtitles:
            ydl_opts.update({
                "writesubtitles": True,
                "writeautomaticsub": True,
                "subtitleslangs": ["es", "en"],
            })

        # Ejecutar descarga en hilo separado
        def _run_download():
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    self._current_ydl = ydl
                    ydl.download([url])
                    
                if not self._cancelled:
                    self.state_callback("success")
                else:
                    self.state_callback("cancelled")
                    
            except Exception as ex:
                if not self._cancelled:
                    self.error_callback(f"Error: {str(ex)}")
                else:
                    self.state_callback("cancelled")
            finally:
                self._current_ydl = None
                self._is_downloading = False

        threading.Thread(target=_run_download, daemon=True).start()