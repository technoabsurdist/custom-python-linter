
class WhiteSpaceError:
    def __init__(self, message, line):
        self.message = message
        self.line = line

    def __str__(self):
        return f"{self.message} on line {self.line}"