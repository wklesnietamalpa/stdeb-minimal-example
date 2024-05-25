import os
from setuptools import setup, find_packages

# Wczytanie opisu z pliku README
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="myscript",
    version="1.1",
    author="Charl P. Botha",
    author_email="cpbotha@vxlabs.com",
    description="Demo of packaging a Python script as DEB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    url="https://github.com/cpbotha/stdeb-minimal-example",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['myscript=myscript.myscript:main']
    },
    data_files=[
        ('share/applications/', ['vxlabs-myscript.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
