from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ConsistentChat",
    version="1.0.0",
    author="Jiawei Chen",
    author_email="jiawei.ucas@gmail.com",
    description="A clean, efficient system for generating multi-turn dialogues using LLM APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chenjiawei30/ConsistentChat",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "dialogue-generator=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["data/*.json", "prompt/*.txt"],
    },
)
