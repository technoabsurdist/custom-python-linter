import argparse
from helpers import parse_file, return_errors

def main():
    # Get name of file as argument (python3 main --file file_name.py)
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="The Python file to lint")
    args = parser.parse_args()
    file_to_lint = args.file

    # Parse python file
    errors_found = parse_file(file_to_lint)

    return_errors(errors_found)
