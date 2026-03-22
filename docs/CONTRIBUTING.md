# Guía de Contribución 🤝

¡Gracias por tu interés en contribuir a video-downloader-library! Este documento te guiará en el proceso.

## Código de Conducta

Por favor, sé respetuoso con los demás contribuidores y usuarios.

## Cómo Contribuir

### Reportar Bugs 🐛

1. Verifica que el bug no haya sido reportado ya en [Issues](https://github.com/tu-usuario/video-downloader-library/issues)
2. Si no existe, crea un nuevo issue con:
   - **Título descriptivo**: "Error al descargar video de YouTube"
   - **Descripción clara**: Qué esperabas y qué sucedió
   - **Pasos para reproducir**: Código mínimo para reproducir el problema
   - **Información del sistema**: SO, versión de Python, versión de yt-dlp
   - **Logs**: Salida de error completa

### Sugerir Mejoras 💡

1. Abre un issue con la etiqueta `enhancement`
2. Describe claramente la mejora propuesta
3. Explica por qué crees que sería útil

### Enviar Pull Requests 📝

#### 1. Fork y Clone

```bash
# Fork el repositorio en GitHub
# Luego en tu máquina:
git clone https://github.com/tu-usuario/video-downloader-library.git
cd video-downloader-library
```

#### 2. Crear una rama

```bash
git checkout -b feature/mi-feature
# o para bugfixes:
git checkout -b bugfix/descripcion-del-bug
```

#### 3. Configurar entorno de desarrollo

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar en modo desarrollo con dependencias de desarrollo
pip install -e ".[dev]"
```

#### 4. Hacer cambios

- **Mantén el código limpio**: Usa PEP 8
- **Agrega type hints**: Para mejor documentación y detección de errores
- **Escribe docstrings**: Para todas las funciones públicas
- **Escribe tests**: Para nuevas funcionalidades

Ejemplo de código estándar:

```python
def fetch_video_info(url: str) -> Dict[str, Any]:
    """Extraer información de video sin descargarlo.
    
    Args:
        url: URL del video.
        
    Returns:
        Diccionario con información del video.
        
    Raises:
        VideoInfoError: Si no se puede obtener la información.
    """
    # Tu implementación aquí
    pass
```

#### 5. Ejecutar tests y verificar formato

```bash
# Ejecutar linter
flake8 video_downloader_library/

# Verificar type hints
mypy video_downloader_library/

# Ejecutar tests
pytest

# Formato automático
black video_downloader_library/
```

#### 6. Commit y Push

```bash
git add .
git commit -m "Add: descripción clara del cambio"
git push origin feature/mi-feature
```

**Mensajes de commit:**
- `Add:` para nuevas características
- `Fix:` para correcciones de bugs
- `Improve:` para mejoras
- `Docs:` para documentación
- `Test:` para tests
- `Refactor:` para reorganización de código

Ejemplo:
```
Add: Soporte para cancelar descargas de forma segura

- Agrega método cancel() a VideoDownloader
- Implementa limpieza de recursos
- Incluye pruebas unitarias
- Actualiza documentación
```

#### 7. Pull Request

1. Ve a tu fork en GitHub
2. Haz click en "New Pull Request"
3. Añade descripción clara de los cambios
4. Referencia cualquier issue relacionado (ejemplo: "Fixes #123")
5. Espera revisión del mantenedor

## Estándares de Código

### Python Style Guide

- Sigue [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Usa `black` para formato automático
- Usa `flake8` para linting

### Type Hints

Todos los parámetros y returns deben tener type hints:

```python
from typing import Dict, List, Optional, Callable

def download(
    self,
    url: str,
    quality: str = "720p",
    callback: Optional[Callable] = None
) -> None:
    """Descargar video."""
    pass
```

### Docstrings

Usa formato Google docstring:

```python
def funcion(param: str) -> Dict[str, Any]:
    """Descripción breve de una línea.
    
    Descripción más detallada si es necesaria. Explica qué hace,
    cómo funciona y casos de uso especiales.
    
    Args:
        param: Descripción del parámetro.
        
    Returns:
        Descripción del valor retornado.
        
    Raises:
        ValueError: Si param es inválido.
        
    Example:
        >>> resultado = funcion("ejemplo")
        >>> print(resultado)
    """
    pass
```

## Proceso de Revisión

Los PR serán revisados por los mantenedores. Pueden solicitar:
- Cambios en el código
- Tests adicionales
- Mejoras en documentación

Por favor, responde a los comentarios de forma constructiva.

## Desarrollo Local

### Estructura de carpetas

```
video-downloader-library/
├── video_downloader_library/     # Código fuente
│   ├── __init__.py
│   ├── video_dowloader.py
│   ├── video_info.py
│   ├── quality_mapper.py
│   ├── exceptions.py
│   └── config.py
├── examples/                     # Ejemplos
├── tests/                        # Tests unitarios
├── docs/                         # Documentación
├── setup.py
├── requirements.txt
└── README.md
```

### Ejecutar el proyecto localmente

```bash
# Instalar en modo desarrollo
pip install -e .

# Ejecutar ejemplos
python examples/basic_usage.py

# Ejecutar tests
pytest -v

# Generar reporte de coverage
pytest --cov=video_downloader_library --cov-report=html
```

## Preguntas y Soporte

- Para preguntas generales: [Discussions](https://github.com/tu-usuario/video-downloader-library/discussions)
- Para bugs: [Issues](https://github.com/tu-usuario/video-downloader-library/issues)
- Para chat: Discord (próximamente)

## Licencia

Al contribuir, aceptas que tus cambios se licencien bajo la misma licencia MIT del proyecto.

¡Gracias por contribuir! 🎉
