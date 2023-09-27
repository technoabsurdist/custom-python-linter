
# '', \n, \t
class WhiteSpaceError:
    def __init__(self, message, file_name, line_number, column_number, code_snippet):
        self.message = message
        self.file_name = file_name
        self.line_number = line_number
        self.column_number = column_number
        self.code_snippet = code_snippet

    def __str__(self):
        # ANSI escape codes for coloring: Red for filename, Green for line and column, Yellow for message
        return f"\n\033[91m{self.file_name}\033[0m:\033[92m{self.line_number}:{self.column_number}\033[0m: \033[93m{self.message}\033[0m -> {self.code_snippet}\n"
