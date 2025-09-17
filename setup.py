"""
Setup script for PyCalcLab - Python Engineering Calculator Library
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
current_directory = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="pycalclab",
    version="0.1.0",
    author="PyCalcLab Contributors",
    author_email="contributors@pycalclab.org",
    description="A comprehensive Python engineering calculator library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/my-sample-org-2025/PyCalcLab",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
        "gui": [
            "tkinter",
            "PyQt5>=5.15.0",
        ],
        "visualization": [
            "plotly>=5.0.0",
            "bokeh>=2.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pycalclab=pycalclab.cli:main",
        ],
    },
    keywords="calculator engineering mathematics science computation",
    project_urls={
        "Bug Reports": "https://github.com/my-sample-org-2025/PyCalcLab/issues",
        "Source": "https://github.com/my-sample-org-2025/PyCalcLab",
        "Documentation": "https://pycalclab.readthedocs.io/",
    },
)