import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deezepy", # Replace with your own username
    version="0.0.1",
    author="CyanBook",
    author_email="lorenzo.delmonte05@gmail.com",
    description="Small Deezer wrapper written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CyanBook/deezepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)