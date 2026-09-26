class Forest_Loc_State():
    _hint_name = "FOREST"

    def __init__(self) -> None:
        self._turn_count = 0
        self._used = False

    @property
    def hint_name(self) -> str:
        return self._hint_name

    @property
    def turn_count(self) -> int:
        return self._turn_count

    @property
    def used(self) -> bool:
        return self._used
    
    # @turn_count.setter
    # def turn_count(self, value: int) -> None:
    #     self._turn_count = value

    # @used.setter
    # def used(self, value: bool) -> None:
    #     self._used = value