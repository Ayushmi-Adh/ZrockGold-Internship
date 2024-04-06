from setuptools import setup, find_packages

setup(
    name='ZrockGold-Internship',
    version='1.0.0',
    author='Ayushmi-Adh',
    description='Music analysis project for ZROCK GOLD internship',
    packages=find_packages(),
    install_requires=[
        'pandas==1.3.5',
        'matplotlib==3.4.3',
        'seaborn==0.11.2'
    ],
)
