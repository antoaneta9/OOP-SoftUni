from project.fish.base_fish import BaseFish
class DeepSeaFish(BaseFish):
    _TIME = 180
    def __init__(self, name: str, points: float):
        super().__init__(name, points, self._TIME)

    def _helper(self):
        return 'DeepSeaFish'