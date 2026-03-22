# Guía: Crear Repositorio en GitHub y Subir Proyecto 🚀

Una guía paso a paso para subir tu librería `video-downloader-library` a GitHub.

## Requisitos Previos

- Cuenta en [GitHub](https://github.com) (crea una si no tienes)
- Git instalado en tu máquina ([descargar aquí](https://git-scm.com/))
- Terminal/CMD con acceso

## Paso 1: Crear Repositorio en GitHub 📝

### 1.1 Acceder a GitHub

1. Ve a [github.com](https://github.com) e inicia sesión
2. Haz click en el ícono **+** en la esquina superior derecha
3. Selecciona **"New repository"**

### 1.2 Configurar el Repositorio

Completa los siguientes campos:

| Campo | Valor |
|-------|-------|
| Repository name | `video-downloader-library` |
| Description | `Una librería personalizada para descargar videos con yt-dlp` |
| Public/Private | **Public** (a menos que quieras privado) |
| Add .gitignore | **NO** (ya tenemos uno) |
| Add a license | **NO** (ya tenemos LICENSE.md) |
| Add README | **NO** (ya tenemos README.md) |

4. Haz click en **"Create repository"**

### 1.3 Copiar la URL

Después de crear el repo, verás una página con opciones. Copia la URL HTTPS o SSH:

```
https://github.com/tu-usuario/video-downloader-library.git
```

## Paso 2: Inicializar Git en tu Proyecto 🔧

En tu terminal, navega a la carpeta del proyecto:

```bash
cd /home/daniel/Documentos/PY_DEV/video_downloader_library
```

### 2.1 Inicializar Git (si aún no está inicializado)

```bash
git init
```

### 2.2 Agregar archivos al staging area

```bash
git add .
```

### 2.3 Crear el primer commit

```bash
git commit -m "Initial commit: Librería para descargar videos con yt-dlp

- Clase VideoDownloader con control de pausa/cancelación
- Soporte para múltiples calidades
- Descarga de subtítulos automáticos
- Documentación completa
- Ejemplos de uso"
```

## Paso 3: Conectar con GitHub 🌐

### 3.1 Agregar remote al repositorio

Reemplaza `tu-usuario` con tu usuario de GitHub:

```bash
git remote add origin https://github.com/tu-usuario/video-downloader-library.git
```

### 3.2 Verificar la conexión

```bash
git remote -v
```

Deberías ver:
```
origin  https://github.com/tu-usuario/video-downloader-library.git (fetch)
origin  https://github.com/tu-usuario/video-downloader-library.git (push)
```

## Paso 4: Subir el Proyecto ⬆️

### 4.1 Cambiar rama a main (importante)

```bash
git branch -M main
```

### 4.2 Hacer push al repositorio

```bash
git push -u origin main
```

**Para las siguientes actualizaciones:**
```bash
git push
```

### 4.3 Si pide credenciales

**Opción A: Token de acceso personal (recomendado)**

1. En GitHub, ve a **Settings → Developer settings → Personal access tokens**
2. Haz click en **"Generate new token"**
3. Selecciona: `repo`, `read:user`, `user:email`
4. Genera el token y cópialo
5. En la terminal, cuando pida contraseña, pega el token

**Opción B: Conexión SSH (más segulo a largo plazo)**

1. Genera clave SSH:
```bash
ssh-keygen -t ed25519 -C "tu.email@example.com"
```

2. Agrega la clave pública a GitHub:
   - Ve a **Settings → SSH and GPG keys**
   - Haz click en **"New SSH key"**
   - Pega tu clave pública (cat ~/.ssh/id_ed25519.pub)

3. Cambia la URL del remote:
```bash
git remote set-url origin git@github.com:tu-usuario/video-downloader-library.git
```

## Paso 5: Configurar tu Perfil en Git 🔐

Si es la primera vez que usas Git:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@example.com"
```

Ver configuración:
```bash
git config --global --list
```

## Paso 6: Actualizar Archivos en el Proyecto 📄

Necesitas actualizar algunos archivos con tu información:

### 6.1 Actualizar `__init__.py`

En `video_downloader_library/__init__.py`, reemplaza:

```python
__author__ = "Tu Nombre"
__email__ = "tu.email@example.com"
```

### 6.2 Actualizar `setup.py`

```python
author="Tu Nombre",
author_email="tu.email@example.com",
url="https://github.com/tu-usuario/video-downloader-library",
```

### 6.3 Actualizar `README.md`

Cambia los siguientes campos:
- `tu-usuario` por tu usuario de GitHub
- `Tu Nombre` por tu nombre
- `tu.correo@example.com` por tu correo

### 6.4 Actualizar `LICENSE`

Reemplaza `Tu Nombre` por tu nombre y el año actual

### 6.5 Actualizar `CONTRIBUTING.md`

Reemplaza `tu-usuario` por tu usuario de GitHub en todos los enlaces

### Hacer commit con estos cambios

```bash
git add .
git commit -m "Update: Agregar información de autor y contacto"
git push
```

## Paso 7: Configuración Adicional en GitHub (Opcional) ⚙️

### 7.1 Agregar Topics

1. Ve a tu repositorio en GitHub
2. Haz click en **"⚙️ Settings"** (a la derecha del repo)
3. Bajo "About", agrega topics:
   - `yt-dlp`
   - `youtube`
   - `video-downloader`
   - `python`
   - `python-library`

### 7.2 Agregar una Descripción

En la sección "About" del repo, agrega:
```
Una librería personalizada para descargar videos desde YouTube y otras plataformas con control de pausa, cancelación y múltiples opciones de calidad.
```

### 7.3 Habilitar Discussions (Opcional)

1. Ve a **Settings → Features**
2. Marca **"Discussions"** (para que otros puedan hacer preguntas)

### 7.4 Crear Releases (Cuando hayas terminado v1.0.0)

```bash
# Crear un tag
git tag -a v1.0.0 -m "Versión 1.0.0: Lanzamiento inicial"

# Subir el tag
git push origin v1.0.0
```

En GitHub:
1. Ve a **Releases**
2. Haz click en **"Create a new release"**
3. Selecciona el tag `v1.0.0`
4. Agrega descripción y cambios

## Paso 8: Flujo de Trabajo Futuro 🔄

### Para actualizar el proyecto

```bash
# 1. Hacer cambios en los archivos
# 2. Ver qué cambió
git status

# 3. Agregar cambios
git add .

# 4. Crear un commit
git commit -m "Type: Descripción del cambio"

# 5. Subir a GitHub
git push
```

### Ramas para features grandes

```bash
# Crear rama para nueva feature
git checkout -b feature/nombre-feature

# ... hacer cambios ...

git add .
git commit -m "Add: Descripción de feature"
git push origin feature/nombre-feature

# En GitHub, abre un Pull Request para mergearlo a main
```

## Especificaciones de Commits 📝

Usa este formato para mensajes de commit:

```
Type: Descripción breve en presente

Descripción detallada (opcional). Explica qué, por qué y cómo.
Puede incluir múltiples líneas si es necesario.

Fixes #123          (opcional: cierra issues)
Related to #456     (opcional: relacionado con issues)
```

**Types válidos:**
- `Add:` - Nueva funcionalidad
- `Fix:` - Corrección de bug
- `Improve:` - Mejora de código existente
- `Refactor:` - Reorganización sin cambios funcionales
- `Docs:` - Cambios en documentación
- `Test:` - Agregar o mejorar tests
- `Chore:` - Cambios en configuración, dependencias, etc.

**Ejemplos:**

```bash
git commit -m "Add: Soporte para convertir formatos de video"
git commit -m "Fix: Error al manejar URLs inválidas"
git commit -m "Docs: Actualizar README con ejemplos avanzados"
```

## Troubleshooting 🔧

### "fatal: not a git repository"

Ejecuta en la carpeta correcta:
```bash
cd /home/daniel/Documentos/PY_DEV/video_downloader_library
```

### "Permission denied (publickey)"

Usa HTTPS en lugar de SSH:
```bash
git remote set-url origin https://github.com/tu-usuario/video-downloader-library.git
```

### "fatal: branch 'main' does not have upstream tracking information"

Usa:
```bash
git push -u origin main
```

### "The file will have its original line endings in your working directory"

Git está transformando line endings. Para Windows:
```bash
git config --global core.autocrlf true
```

Para Linux/Mac:
```bash
git config --global core.autocrlf input
```

### Ver historial de commits

```bash
git log --oneline
```

### Deshacer último commit (si no fue pushed)

```bash
git reset --soft HEAD~1
```

### Ver cambios sin hacer commit

```bash
git diff
```

## Siguiente Paso: Publicar en PyPI 📦

Una vez que tu librería esté en GitHub, puedes publicarla en PyPI (Python Package Index) para que otros puedan instalarla con `pip`:

```bash
pip install video-downloader-library
```

### Pasos básicos:

1. Crea cuenta en [PyPI.org](https://pypi.org)
2. Instala `twine`: `pip install twine`
3. Construye el paquete: `python setup.py sdist bdist_wheel`
4. Sube a PyPI: `twine upload dist/*`

(Esto será una guía separada más detallada)

## Checklist Final ✅

- [ ] Repositorio creado en GitHub
- [ ] Código subido a GitHub
- [ ] README.md con instrucciones completas
- [ ] LICENSE incluido (MIT)
- [ ] .gitignore configurado
- [ ] Autor y email actualizados en archivos
- [ ] Topics agregados al repo
- [ ] Descripción del repositorio completada
- [ ] (Opcional) Tag v1.0.0 creado

## Recursos y Links 🔗

- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/es/)

---

¡Felicidades! Tu proyecto está en GitHub y listo para compartir con el mundo! 🎉

Si tienes problemas, abre un issue en el repositorio o consulta la documentación de GitHub.
