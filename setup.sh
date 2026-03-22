#!/bin/bash
# Quick Start Script para video-downloader-library
# Este script configura el proyecto localmente

set -e

echo "🚀 Iniciando configuración de video-downloader-library..."
echo ""

# Verificar Python
echo "📍 Verificando Python..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "✅ Python $python_version detectado"
echo ""

# Crear virtual environment si no existe
if [ ! -d "venv" ]; then
    echo "📍 Creando entorno virtual..."
    python -m venv venv
    echo "✅ Entorno virtual creado"
else
    echo "✅ Entorno virtual ya existe"
fi
echo ""

# Activar virtual environment
echo "📍 Activando entorno virtual..."
source venv/bin/activate
echo "✅ Entorno virtual activado"
echo ""

# Instalar en modo desarrollo
echo "📍 Instalando paquete en modo desarrollo..."
pip install -e . > /dev/null 2>&1
echo "✅ Paquete instalado"
echo ""

# Instalar dependencias de desarrollo (opcional)
echo "📍 Instalando dependencias de desarrollo..."
pip install -e ".[dev]" > /dev/null 2>&1
echo "✅ Dependencias de desarrollo instaladas"
echo ""

# Verificar instalación
echo "📍 Verificando instalación..."
python -c "from video_downloader_library import VideoDownloader; print('✅ Módulo importado correctamente')"
echo ""

# Mostrar información
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ✅ ¡Configuración completada exitosamente!               ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📦 Próximos pasos:"
echo ""
echo "1. Ejecutar ejemplos:"
echo "   python examples/basic_usage.py"
echo ""
echo "2. Explorar la documentación:"
echo "   cat docs/README.md"
echo ""
echo "3. Preparar para GitHub (ver GITHUB_SETUP.md):"
echo "   cat docs/GITHUB_SETUP.md"
echo ""
echo "4. Ver resumen de mejoras implementadas:"
echo "   cat docs/RESUMEN.md"
echo ""
echo "💡 Tip: El entorno virtual está activado."
echo "   Para desactivarlo, ejecuta: deactivate"
echo ""
