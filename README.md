# Generating ASCII directory trees in Python 

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction

Have you ever wanted to generate a directory tree in ASCII format? Whether it's for a README file, a CLI outuput, asking help or even for a ChatGPT prompt! Well, FASO was created to help you with that. It's a simple Python program that allows you to generate a directory tree in ASCII format with just a single command and a few arguments.

## Installation

You can install FASO by downloading the source code from this repository and running the `faso.py` file with the arguments shown in the [usage](#usage) section.

## Usage

To use FASO, simply run the following command in your terminal:

```cmd
usage: faso.py [-h] [--extension EXTENSION] [--depth DEPTH] [--color] [--permissions] [--human-readable] [--log LOG] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] directory

Generate a directory tree in ASCII format.

positional arguments:
  directory             The directory path to generate the tree for.

options:
  -h, --help            show this help message and exit
  --extension EXTENSION, -e EXTENSION
                        Filter files by extension.
  --depth DEPTH, -d DEPTH
                        Limit the depth of the tree traversal.
  --color               Enable colorized output.
  --permissions         Show file/directory permissions.
  --human-readable, -hr
                        Show file sizes in a human-readable format.
  --log LOG, -l LOG     Log file path (default: tree.log).
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level (default: INFO).
```

## Examples

Here are some examples of how you can use FASO:

```cmd
python faso.py C:\Users\user\Documents\GitHub\faso
```
This will generate a directory tree for the `faso` directory and all of its subdirectories.

```cmd
python faso.py C:\Users\user\Documents\GitHub\faso -e .py -d 2 --color --permissions --human-readable
```
This will generate a directory tree for the `faso` directory and all of its subdirectories, but only show files with the `.py` extension and limit the depth of the tree traversal to 2. It will also colorize the output, show file/directory permissions, and show file sizes in a human-readable format.

```cmd
python faso.py C:\Users\user\Documents\GitHub\faso -e .py -d 2 --color --permissions --human-readable -l
```

Same as the previous example, but it will also log the output to a file called `tree.log`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.