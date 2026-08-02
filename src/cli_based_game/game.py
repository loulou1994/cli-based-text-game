from typing import List
from game_types import Location
from player import Player
from utils import typed_random_word

class Game(object):
    def __init__(self, locations: List[tuple[str, Location]], player: Player, random_messages: dict) -> None:
        self.__locations = locations
        self.__current_location = self.__locations[0][1]
        self.__current_possible_destinations = self.__current_location["destinations"]
        self.__welcome_msg = "Welcome to the cave adventure clone game, hope you'll have a great chilling time while here hihi!!"
        self.__player = player
        self.__random_messages = random_messages
        self.__previous_location = None
        # self.destinations = destinations
        # self.locations_descr = locations_descr
        
    def run(self):
            print(f"{self.__welcome_msg}\n")

            while True:
                player_action = input(f"{self.__current_location["description"]}\n\n> ")

                try:
                    typed_random_word(player_action,self.__random_messages)
                    chosen_destination = self.__player.move(player_action, self.__current_possible_destinations)
                    print(f"chosen destination is {chosen_destination}")
                    
                except ValueError as err:
                    print(f"{err}\n")
                            
                except Exception as err:
                    print(f"An unexpected error happened`\n{err}")