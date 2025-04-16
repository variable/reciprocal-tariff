from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="reciprocal-tariff",
    version="1.0.0",
    author="Python Anti-Economist",
    author_email="james@lin.net.nz",
    description="Make importing shit again! A parody package that imposes tariffs on tariff imports.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/variable/reciprocal-tariff",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    keywords="import, tariff, parody, monkey-patch",
) 