from functions.functions import *
import setup.arguments as a


def main():
    """
    Parameters: takes no parameters
    Reads into a file
    Parses content and writes it to a new .txt file
    Return none
    """
    tasks = read_file(a.filename)
    write_file(tasks)


if __name__ == "__main__":
    main()
