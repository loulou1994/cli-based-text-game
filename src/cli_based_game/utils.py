import yaml

def typed_random_word(input: str, random_messages: dict) -> None:
    if input in random_messages:
        raise ValueError(random_messages[input])

def parse_locations_and_destionations():
    try:
        with open("game_data.yaml", encoding="utf-8") as file: 
            db = yaml.safe_load(file)

            locations, motions = [], []
            for location in db["LOCATIONS"]:
                locations.append(location)
            
            for _, movements in db["MOVEMENTS"].items():
                motions.extend(movements)
                
            return (locations, motions)
        
    except FileNotFoundError as err:
        print(f"The file couldn't be resolved:\n{err}")
        exit(1)

    except Exception as err:
        print(f"An error happened:\n{err}")
        exit(1)