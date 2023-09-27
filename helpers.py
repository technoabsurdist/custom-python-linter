# Helper functions for main
from typing import List
from errors import WhiteSpaceError

def parse_file(file_to_lint):
    with open(file_to_lint, 'r') as f:
        lines = f.readlines()

    errors = []
    for i, line in enumerate(lines):
        # Check for leading whitespace
        if line.startswith((' ', '\t')):
            column_number = 1  
            error_leading = WhiteSpaceError("Leading whitespace found", file_to_lint, i + 1, column_number, line.strip())
            errors.append(error_leading)
        
        # Check for trailing whitespace
        stripped_line = line.rstrip('\n')
        if stripped_line != line.rstrip():
            column_number = len(stripped_line) + 1 
            error_trailing = WhiteSpaceError("Trailing whitespace found", file_to_lint, i + 1, column_number, line.strip())
            errors.append(error_trailing)

    return errors




def return_errors_formatted(errors: List[WhiteSpaceError]):
    for error in errors:
        print(error)

