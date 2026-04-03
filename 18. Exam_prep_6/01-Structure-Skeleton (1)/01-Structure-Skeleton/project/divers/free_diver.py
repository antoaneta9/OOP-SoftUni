from project.divers.base_diver import BaseDiver
class FreeDiver(BaseDiver):
    _OXYGEN_LEVEL = 120
    def __init__(self, name: str):
        super().__init__(name, self._OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        oxygen_to_lose = round(time_to_catch * 0.60)
        if self.oxygen_level < oxygen_to_lose:
            self.oxygen_level = 0
            return
        self.oxygen_level -= oxygen_to_lose
    def renew_oxy(self):
        self.oxygen_level = self._OXYGEN_LEVEL
