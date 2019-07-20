import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grtoolkit",
    version="19.07.4",
    author="Gabriel Rosales",
    author_email="gabriel.alejandro.rosales@gmail.com",
    description="Common functions for quick python development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZenosParadox/grtoolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)