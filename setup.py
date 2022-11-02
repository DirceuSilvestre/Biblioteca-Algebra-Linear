from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Algebra_Linear",
    version="0.0.1",
    author="Dirceu Silvestre",
    author_email="dirceu_silvestre@hotmail.com",
    description="Biblioteca com funções que geram e calculam vetores e matrizes",
    long_description="",
    long_description_content_type="",
    url="https://github.com/DirceuSilvestre/Biblioteca-Algebra-Linear",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)