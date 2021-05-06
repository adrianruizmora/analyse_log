import argparse
import sys


parser = argparse.ArgumentParser(
    "Filters logs and writes output into a new file")
parser.add_argument("-f", "--file", type=str, help="file path")
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    sys.exit("Error : missing command line arguments, try -h for help.")
