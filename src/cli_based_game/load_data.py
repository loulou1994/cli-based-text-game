from typing import List
import yaml
from cli_based_game.hints import List_Of_Hint_States, Hint_State_Factory, N_HINTS, List_Of_Hints, Hint_Factory
from .location_types import Location
from .lookups import Hint_Locations

def parse_game_db():
    try:
        with open("game_db.yaml", encoding="utf-8") as file:
            db = yaml.safe_load(file)

            locations: List[Location] = []
            motions: List[List[str]] = []
            actions: List[List[str]] = []
            arbitrary_messages: List[str] = []
            location_hint_states: List_Of_Hint_States = [[] for _ in range(N_HINTS)]
            hints: List_Of_Hints = []

            for loc_name, location in db["Locations"]:
                # the pipe symbol merges two dic and creates a brand new one
                locations.append(location | {"name": loc_name})
                
                if "hint" in location:
                    location_hint_state = Hint_State_Factory.initialize_hint_state(location["hint"], location)
                    location_hint_states[Hint_Locations[location["hint"]].value].append(location_hint_state)
            
            for motion in db["Movements"]:
                motions.append(motion[1])

            for _, message in db["Arbitrary_Messages"]:
                arbitrary_messages.append(message)

            # for msg_key in ArbitraryMessages:
            #     arbitrary_messages.append(db["Arbitrary_Messages"][msg_key.name])

            for action in db["Actions"]:
                actions.append(action[1])

            for _hint_name, hint in db["Hints"]:
                hints.append(Hint_Factory.initialize_hint(_hint_name, hint))

            file.close()
            return (locations, location_hint_states, motions, actions, arbitrary_messages, hints)

    except KeyError as err:
        print(f"Parsing game data error:\nTried to access a non-existant key {err}")
        exit(1)

    except FileNotFoundError as err:
        print(f"Parsing game data error:\nThe file couldn't be resolved:\n{err}")
        exit(1)

    except Exception as err:
        print(f"Parsing game data error:\n{err}")
        exit(1)

locations, location_hint_states, motions, actions, arbitrary_messages, hints = parse_game_db()