"""Ejemplos básicos de uso de la librería video-downloader-library."""

import sys
import os
from pathlib import Path

# Agregar la ruta del módulo actual al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from video_downloader_library import VideoDownloader, fetch_video_info


def example_1_basic_download():
    """Ejemplo 1: Descarga básica de un video."""
    print("\n" + "=" * 60)
    print("Ejemplo 1: Descarga Básica")
    print("=" * 60)
    
    def on_progress(pct, filename, downloaded, total, speed):
        """Callback de progreso."""
        speed_mb = speed / (1024 * 1024)
        total_mb = total / (1024 * 1024)
        downloaded_mb = downloaded / (1024 * 1024)
        print(
            f"\r{filename}: {pct*100:6.1f}% "
            f"({downloaded_mb:6.1f}/{total_mb:6.1f} MB) "
            f"@ {speed_mb:5.1f} MB/s",
            end=""
        )
    
    def on_state(state):
        """Callback de estado."""
        print(f"\nEstado: {state}")
    
    def on_error(error):
        """Callback de error."""
        print(f"\nError: {error}")
    
    # URL de ejemplo (video corto)
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    downloader = VideoDownloader(None, on_progress, on_state, on_error)
    print(f"Descargando: {url}")
    print("Calidad: 720p, Subtítulos: No")
    downloader.download(url, "720p", False)
    
    # Esperar a que termine
    while downloader.is_downloading():
        import time
        time.sleep(0.5)


def example_2_get_video_info():
    """Ejemplo 2: Obtener información del video."""
    print("\n" + "=" * 60)
    print("Ejemplo 2: Obtener Información del Video")
    print("=" * 60)
    
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    print(f"Obteniendo información de: {url}")
    info = fetch_video_info(url)
    
    print(f"\nTítulo: {info['title']}")
    print(f"Duración: {info['duration']} segundos ({info['duration']//60} minutos)")
    print(f"Miniatura: {info['thumbnail']}")
    print(f"\nTamaños disponibles por calidad:")
    for quality, size in info['sizes'].items():
        print(f"  {quality:12s}: {size:>6s}")


def example_3_pause_resume():
    """Ejemplo 3: Pausa y reanudación."""
    print("\n" + "=" * 60)
    print("Ejemplo 3: Pausa y Reanudación")
    print("=" * 60)
    print("NOTA: Este ejemplo requiere pausar manualmente durante la descarga")
    
    import time
    
    def on_progress(pct, filename, downloaded, total, speed):
        speed_mb = speed / (1024 * 1024)
        status = "(PAUSADO)" if downloader.is_paused() else "(DESCARGANDO)"
        print(f"{status} {pct*100:.1f}% @ {speed_mb:.1f} MB/s", end="\r")
    
    def on_state(state):
        print(f"\nEstado: {state}")
    
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    downloader = VideoDownloader(None, on_progress, on_state, print)
    
    print(f"Descargando: {url}")
    downloader.download(url, "360p", False)
    
    # Simular pausa y reanudación
    time.sleep(2)
    if downloader.is_downloading():
        print("\nPausando descarga...")
        downloader.pause()
        time.sleep(2)
        print("Reanudando descarga...")
        downloader.resume()
    
    # Esperar a que termine
    while downloader.is_downloading():
        time.sleep(0.5)


def example_4_different_qualities():
    """Ejemplo 4: Descargar en diferentes calidades."""
    print("\n" + "=" * 60)
    print("Ejemplo 4: Diferentes Calidades")
    print("=" * 60)
    
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    qualities = ["best", "720p", "360p"]
    
    def on_progress(pct, filename, downloaded, total, speed):
        print(f"  {pct*100:5.1f}%", end="\r")
    
    downloader = VideoDownloader(None, on_progress, None, print)
    
    # Obtener información primero
    info = fetch_video_info(url)
    print(f"Video: {info['title']}")
    print(f"\nTamaños por calidad:")
    for quality, size in info['sizes'].items():
        print(f"  {quality:12s}: {size:>6s}")
    
    # Descomentar para descargar realmente
    # for quality in qualities:
    #     print(f"\nDescargando en {quality}...")
    #     downloader.download(url, quality, False)
    #     while downloader.is_downloading():
    #         time.sleep(0.5)


def example_5_with_subtitles():
    """Ejemplo 5: Descargar con subtítulos."""
    print("\n" + "=" * 60)
    print("Ejemplo 5: Descargar con Subtítulos")
    print("=" * 60)
    
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    def on_progress(pct, filename, downloaded, total, speed):
        print(f"{pct*100:6.1f}%", end="\r")
    
    def on_state(state):
        print(f"\nEstado: {state}")
    
    downloader = VideoDownloader(None, on_progress, on_state, print)
    
    print(f"Descargando: {url}")
    print("Calidad: 720p, Subtítulos: Español + Inglés")
    # downloader.download(url, "720p", True)  # Descomentar para ejecutar
    
    print("\nNota: Los subtítulos se descargaran en archivos .vtt")
    print("Idiomas soportados: es, en (configurable)")


def main():
    """Función principal con menú de ejemplos."""
    print("\n" + "=" * 60)
    print("EJEMPLOS DE VIDEO-DOWNLOADER-LIBRARY")
    print("=" * 60)
    print("\n1. Obtener información del video (recomendado primero)")
    print("2. Descarga básica (comentado para no descargar automáticamente)")
    print("3. Pausa y reanudación (comentado)")
    print("4. Diferentes calidades (comentado)")
    print("5. Con subtítulos (comentado)")
    print("\nEjecutando ejemplo 2 (información del video)...")
    
    # Ejecutar ejemplo de información (no requiere descarga)
    example_2_get_video_info()
    
    print("\n" + "=" * 60)
    print("✅ Ejemplos completados")
    print("=" * 60)
    print("\nDescomenta el código en los ejemplos para ejecutar descargas reales.")
    print("URL de prueba: https://www.youtube.com/watch?v=dQw4w9WgXcQ")


if __name__ == "__main__":
    main()
