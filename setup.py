import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("deeq/_version.py", "r", encoding="utf-8") as f:
    exec(f.read())

with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = list(map(str.strip, f))

setuptools.setup(
    name = "deeq",
    version=__version__,
    author="The Deeq Developers",
    author_email="info@deeq.com",
    description="Quantum Computer Library for Everyone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Deeq/Deeq",
    license="Apache 2",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
    ]
)
