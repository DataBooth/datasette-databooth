# datasette-databooth

[![PyPI](https://img.shields.io/pypi/v/datasette-databooth.svg)](https://pypi.org/project/datasette-databooth/)
[![Changelog](https://img.shields.io/github/v/release/DataBooth/datasette-databooth?include_prereleases&label=changelog)](https://github.com/DataBooth/datasette-databooth/releases)
[![Tests](https://github.com/DataBooth/datasette-databooth/workflows/Test/badge.svg)](https://github.com/DataBooth/datasette-databooth/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/DataBooth/datasette-databooth/blob/main/LICENSE)

DataBooth extensions to Datasette

## Installation

Install this plugin in the same environment as Datasette.

    $ datasette install datasette-databooth

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-databooth
    python3 -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
