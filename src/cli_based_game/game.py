from typing import List
from cli_based_game import locations, arbitrary_messages, Locations, ArbitraryMessages, Location, Destination, InputWordError
# from exceptions import InputWordError
from .player import Player, Player_State

class Game(object):
    def __init__(self) -> None:
        self._current_location: Location = locations[0]
        self._current_destinations: List[Destination] = self._current_location["destinations"]
        self._prompt_desc = f"{arbitrary_messages[ArbitraryMessages.WELCOME_MSG.value]}"
        self._player = Player()
        self._previous_location = None
        # self.destinations = destinations
        # self.locations_descr = locations_descr
        
    def run(self):
            # print(self._prompt_desc)
            
            while True:
                self.output_current_prompt()
                try:
                    player_input = input("> ")
                    self._player.update_player_state(player_input)
                    self.handle_player_action(player_input)

                except InputWordError as err:
                    self._prompt_desc = str(err)
                    continue

                except KeyboardInterrupt:
                    print()
                    exit(1)

                except Exception as err:
                    print(f"An unexpected error happened\n{str(err)}")
                    exit(1)

    def move_to_new_location(self, new_location: Location) -> None:
        self._previous_location = self._current_location
        self._current_location = new_location
        self._current_destinations = self._current_location["destinations"]

    def back_to_prev_location(self):
        if not self._previous_location:
            return False
        
        if any(condition in self._current_location["conditions"] for condition in {"forest", "back"}):
            return False

        self._current_location, self._previous_location = self._previous_location, self._current_location
        return True

    def handle_player_action(self, player_input: str):
        match self._player.state:
            case Player_State.WALKING:
                destination = self._player.move(player_input, self._current_destinations)
                self.move_to_new_location(locations[Locations[destination].value])
                self._prompt_desc = self._current_location["description"]
            
            case Player_State.WALKING_BACK:
                can_go_back = self.back_to_prev_location()
                self._prompt_desc = self._current_location["description"] if can_go_back else arbitrary_messages[ArbitraryMessages.NO_BACK.value]

            case _:
                raise ValueError("Couldn't figure out your move!")
    
    def output_current_prompt(self):
        print()
        print(self._prompt_desc)
        print()