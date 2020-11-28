from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
dependencies = [
    'cycler>=0.10.0',
    'kiwisolver>=1.3.1',
    'matplotlib>=3.3.3',
    'numpy>=1.19.4',
    'Pillow>=8.0.1',
    'pyparsing>=2.4.7',
    'python-dateutil>=2.8.1',
    'six>=1.15.0'
]

setup(
    name="cambrac",
    version="0.0.1",
    author="Arma",
    author_email="Arma@Jangal.co",
    description="Compare Add Two Matrix by Row & Col",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LordArma/cambrac",
    install_requires=dependencies,
    license='MIT License',
    packages=find_packages(),
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)
