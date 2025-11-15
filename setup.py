from setuptools import setup


with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name="diff_as_git",
    version="0.0.1",
    license="MIT License",
    author="Lucas de Souza e Sousa",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="lucas11souza97@gmail.com",
    keywords="basic components python projcts",
    description="This project aims to share components and features that would be replicated in most Python projects.",
    packages=["diff_as_git"],
    install_requires=["requests"],
)
