
THIS PROJECT IS DISCONTINUED AND WILL BE ELIMINATED!!


# Starseeker - utils
## A collection of OS utilities written in Python

utils is meant to be a small CLI program to handle easy scripting issues, any forks or pull requests are welcomed!

### What I use for virtual environment management

I prefer to use poetry, but I believe pipenv is better for production environments. This small, personal project uses pipenv.
A requirements.txt has been provided in case you want to build dependencies by other means.

Make sure you have poetry:

        pip install pipenv
    
And then, create the virtual environment and handle dependencies:

        pipenv install

### Tests

All tests are found in ./tests, my tool of choice tends to be, hypothesis, tox or pytest with plugins. I've used doctest in this case, as a way of learning the tool myself.
*In my opinion, doctesting isn't as efficient as unittesting, specially with libraries like pytest*.

To run any test, just use:

    sh tests.sh

### Running the app

This is a CLI app, make sure you built the needed dependencies. To start the app just run:

    sh start.sh

That shell file just automates the following command:

    pipenv run python3 main.py
### Using the app

There's a main screen that leads to every app, you can return to it using:

    RETURN

or

    GO BACK

Similarly, you can exit the app at any time using:

    EXIT

