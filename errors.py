# Generic error for all errors inheritance
class Error:
    def __init__(self, message, file_name, line_number, column_number):
        self.message = message
        self.file_name = file_name
        self.line_number = line_number
        self.column_number = column_number

    def __str__(self):
        return f"\n\033[91m{self.file_name}\033[0m:\033[92m{self.line_number}:{self.column_number}\033[0m: \033[93m{self.message}\033[0m\n"

class WhiteSpaceError(Error):
    def __init__(self, message, file_name, line_number, column_number, code_snippet):
        super().__init__(message, file_name, line_number, column_number)
        self.code_snippet = code_snippet

    def __str__(self):
        return super().__str__() + f" -> {self.code_snippet}"

class CustomSyntaxError(Error):
    def __init__(self, message, file_name, line_number, column_number):
        super().__init__(message, file_name, line_number, column_number)

    def __str__(self):
        return super().__str__()