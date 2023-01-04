# Starseeker - utils
## A collection of OS utilities written in Python

utils is meant to be a small CLI program to handle easy scripting issues, any forks or pull requests are welcomed!

### What I use for virtual environment management

I prefer to use poetry, but I believe pipenv is better for production environments. This small, personal project uses poetry.
A requirements.txt has been provided in case you want to build dependencies by other means.

Make sure you have poetry:

        pip install poetry
    
And then, create the virtual environment and handle dependencies:

        poetry install
        poetry shell
### Tests

All tests are found in ./tests, my tool of choice tends to be, hypothesis, tox or pytest with plugins. I've used doctest in this case, as a way of learning the tool myself.
*In my opinion, doctesting isn't as efficient as unittesting, specially with libraries like pytest*.

To run any test, just use:

    make doctest

### Running the app

This is a CLI app, make sure you built the needed dependencies. To start the app just run:

        python main.py

### Using the app

