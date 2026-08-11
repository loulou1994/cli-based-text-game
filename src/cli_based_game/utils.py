import yaml
from cli_based_game.game_data_lookups import ArbitraryMessages

def parse_game_db():
    try:
        with open("game_db.yaml", encoding="utf-8") as file:
            db = yaml.safe_load(file)

            locations, motions, arbitrary_messages = [], [], []

            for _, location in db["Locations"]:
                locations.append(location)
            
            for motion_key in db["Movements"]:
                motions.extend(db["Movements"][motion_key])

            for msg_key in ArbitraryMessages:
                arbitrary_messages.append(db["Arbitrary_Messages"][msg_key.name])

            return (locations, motions, arbitrary_messages)

    except KeyError as err:
        print(f"Error! Tried to access a non-existant key {err}")
        exit(1)

    except FileNotFoundError as err:
        print(f"The file couldn't be resolved:\n{err}")
        exit(1)

    except Exception as err:
        print(f"An error happened:\n{err}")
        exit(1)

def typed_random_word(input: str, random_messages: dict) -> None:
    if input in random_messages:
        raise ValueError(random_messages[input])