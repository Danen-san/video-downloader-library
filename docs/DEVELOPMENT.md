# 🧪 Guía de Testing y Desarrollo

Cómo ejecutar tests y mantener el código de calidad.

## Setup para Desarrollo

```bash
# Instalar en modo desarrollo con dependencias de dev
pip install -e ".[dev]"

# Esto instala:
# - pytest >= 7.0
# - black >= 22.0
# - flake8 >= 4.0
# - mypy >= 0.950
# - pytest-cov >= 3.0
```

## Formato de Código

Usa `black` para formatear automáticamente:

```bash
# Formatear todos los archivos
black video_downloader_library/

# Formatear un archivo específico
black video_downloader_library/video_dowloader.py
```

## Análisis de Código

### Linting con flake8

```bash
# Verificar todo el código
flake8 video_downloader_library/

# Verificar un archivo
flake8 video_downloader_library/video_dowloader.py
```

**Errores comunes:**
- E999: Syntax error
- E501: Línea muy larga
- W503: Operador antes de break

### Type Checking con mypy

```bash
# Verificar tipos
mypy video_downloader_library/

# Verificar un archivo
mypy video_downloader_library/video_dowloader.py
```

## Testing

### Crear tests

Crea archivo `tests/test_quality_mapper.py`:

```python
import pytest
from video_downloader_library.quality_mapper import get_format_selector
from video_downloader_library.exceptions import InvalidQualityError

def test_valid_quality():
    """Test que calidad válida retorna selector correcto"""
    result = get_format_selector("720p")
    assert result == "best[ext=mp4][height<=720]"

def test_invalid_quality():
    """Test que calidad inválida lanza excepción"""
    with pytest.raises(InvalidQualityError):
        get_format_selector("invalid_quality")

def test_all_qualities():
    """Test todas las calidades"""
    qualities = ["best", "720p", "360p", "high_audio", "low_audio"]
    for quality in qualities:
        result = get_format_selector(quality)
        assert isinstance(result, str)
        assert len(result) > 0
```

### Ejecutar tests

```bash
# Todos los tests
pytest

# Tests específicos
pytest tests/test_quality_mapper.py

# Con output detallado
pytest -v

# Con coverage
pytest --cov=video_downloader_library

# Generar reporte HTML
pytest --cov=video_downloader_library --cov-report=html
```

## Pre-commit Hooks (Opcional)

Crear `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.1
    hooks:
      - id: mypy
```

Instalar:

```bash
pip install pre-commit
pre-commit install
```

## Checklist Antes de Commit

- [ ] Código formateado con `black`
- [ ] Sin errores de `flake8`
- [ ] Type hints correctos en `mypy`
- [ ] Tests nuevos para código nuevo
- [ ] Docstrings actualizados
- [ ] README actualizado si es necesario

## Workflow Recomendado

```bash
# 1. Hacer cambios
# editar archivo...

# 2. Formatear
black video_downloader_library/

# 3. Verificar
flake8 video_downloader_library/
mypy video_downloader_library/

# 4. Testear
pytest -v

# 5. Commit
git add .
git commit -m "Type: Descripción"

# 6. Push
git push
```

## Coverage Goals

- Línea: 80%+
- Branch: 75%+
- Main functions: 90%+

Ver reporte:

```bash
pytest --cov=video_downloader_library --cov-report=term-missing
```

## CI/CD (Github Actions)

Crear `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        pip install -e ".[dev]"
    
    - name: Lint with flake8
      run: flake8 video_downloader_library/
    
    - name: Type check with mypy
      run: mypy video_downloader_library/
    
    - name: Test with pytest
      run: pytest --cov=video_downloader_library
```

## Documentación de Código

### Docstring Format (Google Style)

```python
def download(
    self,
    url: str,
    quality: str = "720p"
) -> None:
    """Descargar video.
    
    Describe lo que hace en una línea.
    
    Explicación más detallada si es necesaria.
    
    Args:
        url: Descripción del parámetro.
        quality: Otra descripción.
        
    Returns:
        Lo que retorna (None si no retorna nada).
        
    Raises:
        InvalidURLError: Cuando ocurre este error.
        InvalidQualityError: Cuando ocurre este otro error.
        
    Example:
        >>> downloader.download("https://...")
        >>> print("Download started")
    """
    pass
```

## Debugging

### Logging

```python
import logging

logger = logging.getLogger(__name__)
logger.debug("Mensaje de debug")
logger.info("Información")
logger.warning("Advertencia")
logger.error("Error")
```

### Usar pdb

```python
import pdb

# Pausar ejecución
pdb.set_trace()

# Comandos:
# n - next line
# c - continue
# s - step into
# l - list code
# p var - print variable
```

## Publish to PyPI

Cuando esté listo para publicar:

```bash
# Instalar herramientas
pip install build twine

# Construir paquete
python -m build

# Subir a PyPI
twine upload dist/*
```

## Recursos

- [pytest Documentation](https://docs.pytest.org/)
- [black Documentation](https://black.readthedocs.io/)
- [flake8 Documentation](https://flake8.pycqa.org/)
- [mypy Documentation](https://mypy.readthedocs.io/)

---

¡Happy testing! 🎉
