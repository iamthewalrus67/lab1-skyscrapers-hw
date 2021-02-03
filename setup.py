import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skyscrapers-Bohdan-Ruban",
    version="0.0.1",
    author="Bohdan Ruban",
    author_email="bohdan.ruban@ucu.edu.com",
    description="First task of the first lab work",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamthewalrus67/lab1-skyscrapers-hw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.1',
)
