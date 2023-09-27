import argparse
from helpers import parse_file, return_errors_formatted

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="The Python file to lint")
    args = parser.parse_args()
    file_to_lint = args.file

    # 2) Parse file
    errors_found = parse_file(file_to_lint)
    # print("Errors found: ", errors_found)

    # 3) Print errors formatted to console
    return_errors_formatted(errors_found)

if __name__ == "__main__":
    main()