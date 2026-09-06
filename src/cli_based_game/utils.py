def typed_random_word(input: str, random_messages: dict) -> None:
    if input in random_messages:
        raise ValueError(random_messages[input])