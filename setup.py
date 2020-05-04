import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elegant-csv-numbertheory",
    version="0.0.1",
    author="JP Etcheber",
    author_email="jetcheber@gmail.com",
    description="A helper for CSV filess",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/numbertheory/elegant-csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
