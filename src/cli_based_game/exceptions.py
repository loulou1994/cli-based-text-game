class WordNotFoundError(Exception):

    def __init__(self, word: str):
        super().__init__(f"I don't really get what you intend to do.\nThe word \"{word}\" doesn't appear to be in my vocabulary")