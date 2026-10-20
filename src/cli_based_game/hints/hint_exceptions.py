class InvalidHintTypeError(Exception):
    """Raised when an invalid hint type is encountered."""
    def __init__(self, hint_type: str):
        super().__init__(f"Invalid hint type: {hint_type}")