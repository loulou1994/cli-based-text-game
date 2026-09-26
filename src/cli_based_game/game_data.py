from typing import List
import yaml
from cli_based_game import Location, List_Of_Hint_States, N_HINTS, Hints, Forest_Loc_State

def parse_game_db():
    try:
        with open("game_db.yaml", encoding="utf-8") as file:
            db = yaml.safe_load(file)

            locations: List[Location] = []
            motions: List[List[str]] = []
            actions: List[List[str]] = []
            arbitrary_messages: List[str] = []
            location_hint_states: List_Of_Hint_States = [[] for _ in range(N_HINTS)]

            for _, location in db["Locations"]:
                if "hint" in location:
                    location_hint_states[Hints[location.hint].value].append(Forest_Loc_State())
                    
                locations.append(location)
            
            for motion in db["Movements"]:
                motions.append(motion[1])

            for _, message in db["Arbitrary_Messages"]:
                arbitrary_messages.append(message)

            
            # for msg_key in ArbitraryMessages:
            #     arbitrary_messages.append(db["Arbitrary_Messages"][msg_key.name])

            for action in db["Actions"]:
                actions.append(action[1])

            return (locations, motions, actions, arbitrary_messages)

    except KeyError as err:
        print(f"Paring game data error:\nTried to access a non-existant key {err}")
        exit(1)

    except FileNotFoundError as err:
        print(f"Paring game data error:\nThe file couldn't be resolved:\n{err}")
        exit(1)

    except Exception as err:
        print(f"Paring game data error:\n{err}")
        exit(1)
        
locations, motions, actions, arbitrary_messages = parse_game_db()