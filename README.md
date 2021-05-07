<h3>Log analysis</h3>

## Problem

- Script that can runs in a minimal environement.
- Parses a planning file and writes it in a new file with a .txt extension.
- Script only uses built-in python fonctions.


### Built With

- []()python3.6
- []()argparse
- []()unittest

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- A compatible operating system (e.g. Linux, macOS, Windows).
- python --version 3.6

### File structure
```sh
.
├── README.md
├── functions
│   ├── __init__.py
│   └── functions.py
├── parse_log.py
├── planning.log
├── setup
│   ├── __init__.py
│   ├── arguments.py
│   └── logConfig.py
└── test
    ├── __init__.py
    └── test_functions.py

3 directories, 10 files
```

### Tests

To run the unittests follow this steps.

1. Go to the root directory

```sh
  cd ~/pathToDirectory
```

2. Run

```sh
  python -m unittest -v
```

<!-- USAGE EXAMPLES -->

## Usage

1. To run the program go to the projects root directory

```sh
  cd ~/pathToFDirectory
```

2. Run the program with required arguments

```sh
  python parse_log.py -f <file.log>
```

3. Example:

```sh
  python parse_log -f planning.log
```

- A file name output.txt will be createad containing the new filtered logs.
- A parse_log.log will also be created containing the logs of the script.

<!-- CONTACT -->

## Contact

Adrian R
06.41.26.70.01
adrianruizmora@gmai.com
