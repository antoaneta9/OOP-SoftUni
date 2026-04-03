from project.teams.base_team import BaseTeam

class OutdoorTeam(BaseTeam):
    _BUDGET = 1000.0
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self._BUDGET)

    def win(self):
        self.advantage += 115
        self.wins += 1

