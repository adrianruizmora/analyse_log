from functions.functions import *
import setup.arguments as a


def main():
    """
    Parses content and writes it to a new .txt file
    
    :param: takes no parameters
    :returns: none
    """
    tasks = read_file(a.filename)
    write_file(tasks)


if __name__ == "__main__":
    main()
