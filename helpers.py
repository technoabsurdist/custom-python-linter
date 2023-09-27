# Helper functions for main
from typing import List
from errors import WhiteSpaceError

def parse_file(file_to_lint):
    with open(file_to_lint, 'r') as f:
        lines = f.readlines() 

    errors = []
    for i, line in enumerate(lines):
        if line != line.rstrip():
            error_whitespace = WhiteSpaceError("Trailing whitespace", i+1)
            errors.append(error_whitespace)
        if '\t' in line:
            error_tab = WhiteSpaceError("Tab character found on line", i+1)
            errors.append(error_tab)

    return errors


def return_errors_formatted(errors: List[WhiteSpaceError]):
    for error in errors:
        print(error)

