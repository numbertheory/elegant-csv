import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elegant-csv-numbertheory",
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
    setup_requires=['setuptools_scm'],
    use_scm_version=True
)
