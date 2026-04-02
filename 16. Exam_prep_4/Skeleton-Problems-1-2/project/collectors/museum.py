from project.collectors.base_collector import BaseCollector

class Museum(BaseCollector):
    _AVAILABLE_MONEY = 15000.0
    _AVAILABLE_SPACE = 2000
    def __init__(self, name:str):
        super().__init__(name, self._AVAILABLE_MONEY, self._AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += 1000.0

