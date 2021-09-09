# Ignition

<!--- Badges --->
![GitHub last commit (8.0)](https://img.shields.io/github/last-commit/thecesrom/Ignition/8.0)
[![GitHub contributors](https://img.shields.io/github/contributors/thecesrom/Ignition)](https://github.com/thecesrom/Ignition/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/thecesrom/Ignition)](https://github.com/thecesrom/Ignition/blob/8.0/LICENSE)
[![GitHub downloads](https://img.shields.io/github/downloads/thecesrom/Ignition/total)](https://github.com/thecesrom/Ignition/releases)
[![time tracker](https://wakatime.com/badge/github/thecesrom/Ignition.svg)](https://wakatime.com/badge/github/thecesrom/Ignition)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Imports: flake8](https://img.shields.io/badge/%20imports-flake8-%231674b1?style=flat&labelColor=ef8336)](https://flake8.pycqa.org/en/latest/)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/thecesrom/Ignition/discussions)

Ignition is a set of packages and modules that allows developers to get code completion for Ignition Scripting API scripting functions in their IDE of choice.

# Releases

Check the [releases page](https://github.com/thecesrom/Ignition/releases) and download the one for your current version.

If you can't find it, feel free to submit your request on our [Discussions](https://github.com/thecesrom/Ignition/discussions).

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 2.7.18 ([download here](https://www.python.org/downloads/release/python-2718/))
* You are familiar with [Ignition 8.0 Scripting Functions](https://docs.inductiveautomation.com/display/DOC80/Scripting+Functions)

## Packages

Ignition consists of the following packages:

* java/javax
* system

### java/javax

These are libraries for some Java packages and functions that are imported in `system` packages meant to be used on development environments where no JDK can be installed, and the project interpreter is Python 2.7.

### system

Is a package that includes all Ignition Scripting Functions.

## Installation and usage

To use Ignition, download the code targeted to your desired version from the [releases page](https://github.com/thecesrom/Ignition/releases) and add it as a dependency to your scripting project.

Also, it can be installed by running `pip`. It requires Python 2.7 (we recommend version 2.7.18).

```bash
$ python2 -m pip install ignition-api==8.0.17
```

This will install it as package to your Python installation, which will allow you to call Ignition Scripting functions from Python's REPL, and get code completion using an IDE (we recommend PyCharm).

```bash
Python 2.7.18 (default, Nov  9 2020, 16:23:15) 
[GCC Apple LLVM 12.0.0 (clang-1200.0.32.21)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from __future__ import print_function
>>> import system.util
>>> print(system.util.__doc__)
Utility Functions.

The following functions give you access to view various Gateway and
Client data, as well as interact with other various systems.

>>> system.util.beep()
>>> quit()
```

And to uninstall:
```bash
$ python2 -m pip uninstall ignition-api
```

## Contributing to Ignition

To contribute to Ignition, follow these steps:

1. Fork this repository
2. Create a local copy on your machine
3. Create a branch
4. Make your changes and commit them
5. Push to the original branch
6. Create the pull request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/thecesrom/Ignition/graphs/contributors).

## License

See the [LICENSE](https://github.com/thecesrom/Ignition/blob/HEAD/LICENSE).

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
