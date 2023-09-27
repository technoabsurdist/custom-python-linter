from typing import List
import errors

def lint_file(file_to_lint):
    # whitespace
    errors_whitespace = lint_file_whitespace(file_to_lint)

    # syntax
    errors_syntax = lint_file_syntax(file_to_lint)

    all_errors = errors_whitespace + errors_syntax

    # print out errors
    for error in all_errors:
        print(error)

def lint_file_whitespace(file_to_lint):
    with open(file_to_lint, 'r') as f:
        lines = f.readlines()
    errors_list = []
    for i, line in enumerate(lines):
        if line.startswith((' ', '\t')):
            column_number = 1  
            error_leading = errors.WhiteSpaceError("Leading whitespace found", file_to_lint, i + 1, column_number, line.strip())
            errors_list.append(error_leading)
        stripped_line = line.rstrip('\n')
        if stripped_line != line.rstrip():
            column_number = len(stripped_line) + 1 
            error_trailing = errors.WhiteSpaceError("Trailing whitespace found", file_to_lint, i + 1, column_number, line.strip())
            errors_list.append(error_trailing)
    return errors_list


def lint_file_syntax(file_to_lint):
    stack = []
    errors_list = []
    
    with open(file_to_lint, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in "({[":
                stack.append((char, i+1, j+1))
            elif char in ")}]":
                if len(stack) == 0:
                    errors_list.append(errors.CustomSyntaxError("Unmatched closing character", file_to_lint, i+1, j+1))
                    continue

                last_open, last_line, last_col = stack.pop()
                if (last_open, char) not in [("(", ")"), ("{", "}"), ("[", "]")]:
                    errors_list.append(errors.CustomSyntaxError("Mismatched characters", file_to_lint, last_line, last_col))

    if len(stack) > 0:
        for last_open, last_line, last_col in stack:
            errors_list.append(errors.CustomSyntaxError("Unmatched opening character", file_to_lint, last_line, last_col))

    return errors_list