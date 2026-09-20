class InputWordError(Exception):
    """raised when picked up input can't be handled"""
    def __init__(self, word: str):
        super().__init__(word)

class InputWordUnavailableError(InputWordError):
    """raised when input is correct but is incompatible at the moment"""
    def __init__(self):
        super().__init__("Can't really move with that")

class InputWordNotFoundError(InputWordError):
    """raised when input is not in db"""
    def __init__(self, word: str):
        super().__init__(f"I don't really get what you intend to do.\nThe word \"{word}\" doesn't appear to be in my vocabulary")