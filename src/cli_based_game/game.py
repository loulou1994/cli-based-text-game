from typing import List
from cli_based_game.game_types import Location, Destination
from cli_based_game.game_data_lookups import Locations, ArbitraryMessages
from cli_based_game.game_data import locations, arbitrary_messages
from cli_based_game.player import Player, Player_State
from cli_based_game.utils import typed_random_word

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
            self._prompt_desc += f"\n\n{self._current_location["description"]}"

            while True:
                player_input = input(f"{self._prompt_desc}\n> ")
                
                try:
                    # typed_random_word(player_input,self.__random_messages)
                    chosen_destination = self._player.move(player_input, self._current_destinations)
                    self.move_to_new_location(locations[Locations[chosen_destination].value])
                
                except ValueError as err:
                    print(f"{err}\n")
                     
                except Exception as err:
                    print(f"An unexpected error happened`\n{err}")

    def move_to_new_location(self, new_location: Location) -> None:
        self._previous_location = self._current_location
        self._current_location = new_location
        self._current_destinations = self._current_location["destinations"]

    def back_to_prev_location(self):
        cant_go_back = False

        if "conditions" in self._current_location:
            cant_go_back = any(condition in self._current_location.conditions for condition in {"forest", "back"})

        if cant_go_back or not self._previous_location:
            self._prompt_desc = "Sorry, can't go back from here"
            return

        self._current_location, self._previous_location = self._previous_location, self._current_location