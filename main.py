import argparse
import helpers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="The Python file to lint")
    args = parser.parse_args()
    file_to_lint = args.file

    # Linting logic
    helpers.lint_file(file_to_lint)

if __name__ == "__main__":
    main()