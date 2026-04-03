from project.fish.base_fish import BaseFish
class PredatoryFish(BaseFish):
    _TIME = 90
    def __init__(self, name: str, points: float):
        super().__init__(name, points, self._TIME)

    def _helper(self):
        return 'PredatoryFish'