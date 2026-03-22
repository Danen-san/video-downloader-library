"""Setup configuración para la librería video-downloader-library."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="video-downloader-library",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu.email@example.com",
    description="Una librería personalizada para descargar videos con yt-dlp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/video-downloader-library",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "yt-dlp>=2024.1.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "pytest-cov>=3.0",
        ],
    },
    entry_points={
        "console_scripts": [],
    },
)
