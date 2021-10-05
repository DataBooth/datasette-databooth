from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-databooth",
    description="DataBooth extensions to Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="DataBooth",
    url="https://github.com/DataBooth/datasette-databooth",
    project_urls={
        "Issues": "https://github.com/DataBooth/datasette-databooth/issues",
        "CI": "https://github.com/DataBooth/datasette-databooth/actions",
        "Changelog": "https://github.com/DataBooth/datasette-databooth/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_databooth"],
    entry_points={"datasette": ["databooth = datasette_databooth"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-databooth[test]"],
    python_requires=">=3.6",
)
