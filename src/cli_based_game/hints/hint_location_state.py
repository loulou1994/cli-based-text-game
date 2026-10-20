
class Forest_Hint_State():
    def __init__(self, hint_loc: str) -> None:
        self._hint_loc = hint_loc
        self._turn_count = 0
        self._used = False

    @property
    def turn_count(self) -> int:
        return self._turn_count

    @property
    def used(self) -> bool:
        return self._used
    
    def increment_turn_count(self) -> None:
        self._turn_count += 1

    # @property
        # def hint_loc(self) -> str:
        #     return self._hint_loc

    # @turn_count.setter
    # def turn_count(self, value: int) -> None:
    #     self._turn_count = value

    # @used.setter
    # def used(self, value: bool) -> None:
    #     self._used = value

    # def __repr__(self) -> str:
    #     return f"Maze_Hint_State(hint_loc={self._hint_loc})"

class Maze_Hint_State():
    def __init__(self) -> None:
        # self._hint_loc = hint_loc
        self._turn_count = 0
        self._used = False

    # @property
    # def hint_loc(self) -> str:
    #     return self._hint_loc

    @property
    def turn_count(self) -> int:
        return self._turn_count

    @property
    def used(self) -> bool:
        return self._used

    # def __repr__(self) -> str:
    #     return f"Maze_Hint_State(hint_loc={self._hint_loc})"