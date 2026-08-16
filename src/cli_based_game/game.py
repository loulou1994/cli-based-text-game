from cli_based_game.game_types import Location
from cli_based_game.game_data_lookups import Locations
from cli_based_game.game_data import locations
from cli_based_game.player import Player
from cli_based_game.utils import typed_random_word

class Game(object):
    def __init__(self) -> None:
        self._current_location = locations[0]
        self._current_destinations = self._current_location["destinations"]
        self._welcome_msg = "Welcome to the cave adventure clone game, hope you'll have a great chilling time while here hihi!!"
        self._player = Player()
        self._previous_location = None
        # self.destinations = destinations
        # self.locations_descr = locations_descr
        %
    def run(self):
            print(f"{self._welcome_msg}\n")

            while True:
                player_action = input(f"{self._current_location["description"]}\n\n> ")

                try:
                    # typed_random_word(player_action,self.__random_messages)
                    chosen_destination = self._player.move(player_action, self._current_destinations)
                    self.update_current_location(locations[Locations[chosen_destination].value])

                except ValueError as err:
                    print(f"{err}\n")
                     
                except Exception as err:
                    print(f"An unexpected error happened`\n{err}")


    def update_current_location(self, new_location: Location) -> None:
        self._previous_location = self._current_location
        self._current_location = new_location
        self._current_destinations = self._current_location["destinations"]